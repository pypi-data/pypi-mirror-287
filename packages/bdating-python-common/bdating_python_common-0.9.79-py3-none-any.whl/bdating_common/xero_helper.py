import os
import base64
import logging
from xero_python.api_client import ApiClient, serialize
from xero_python.api_client.oauth2 import OAuth2Token
from xero_python.api_client.configuration import Configuration
from xero_python.accounting import AccountingApi, Contact, LineItem, Account, BankTransaction, BankTransactions, LineItem, Invoice, Invoices, Contacts, AccountType, Currency, CurrencyCode
from functools import wraps
import jwt
from datetime import *
from xero_python.utils import getvalue
from xero_python.exceptions import AccountingBadRequestException
import dateutil
from dateutil.relativedelta import *
from .model import Booking, RefAndCommissionModel, InvoiceStatusEnum, TransactionStatusEnum
from .xero_utils import get_booking_id, get_booking_date
import decimal
import yaml

log = logging.getLogger(__name__)


DIR, _ = os.path.split(os.path.abspath(__file__))
xero_config = {}
with open(os.path.join(DIR, 'xero_config.yml')) as f:
    xero_config = yaml.safe_load(f)


client_id = os.environ.get('XERO_CLIENT_ID', '')
client_secret = os.environ.get('XERO_CLIENT_SECRET', '')
tenant_id = os.environ.get('XERO_TENANT_ID', '')

message_bytes = (client_id + ":" + client_secret).encode("utf-8")
encoded_bytes = base64.b64encode(message_bytes)
encoded_message = encoded_bytes.decode("utf-8")

# scope = "accounting.transactions accounting.transactions.read accounting.contacts accounting.contacts.read"

xero_token = {}

is_debug = False
if os.getenv('DEBUG'):
    is_debug = True

# configure xero-python sdk client
api_client = ApiClient(
    Configuration(
        debug=is_debug,
        oauth2_token=OAuth2Token(
            client_id=client_id, client_secret=client_secret
        ),
    ),
    pool_threads=1,
)



def xero_token_required(function):
    @wraps(function)
    def decorator(*args, **kwargs):
        old_token = get_token()

        return function(*args, **kwargs)

    return decorator

@api_client.oauth2_token_saver
def set_token(token):
    claims = jwt.decode(token["access_token"], options={"verify_signature": False})
    token["expires_at"] = claims["exp"]
    global xero_token
    xero_token = token


@api_client.oauth2_token_getter
def get_token():
    global xero_token
    if xero_token == {} or xero_token['expires_at'] - datetime.now().timestamp() < 60:
        log.info('expired or no token')
        temp_token = api_client.get_client_credentials_token()
        return temp_token
    return xero_token



accounts = {
    'currency_code': CurrencyCode('AUD'),
    'order_receive': 200,
    'platform_commission': 200,
    'referral_commisssion': 200,
    'withdraw': 200,
    'referral_reconciliation': 200,

}
"""
referral_model
[
    {
        uid: 
        referral_config: {
            platform_commission: float
            reward_layers: list[float]
        }
    },
    ...
]
"""
@xero_token_required
async def create_txns_on_order_confirmed(booking: Booking, provider_model: RefAndCommissionModel, referral_models: list[RefAndCommissionModel]):
    summarize_errors = 'True'
    api_instance = AccountingApi(api_client)

    # important to setup accounts first
    if booking['payment_type'] == 'stripe':
        # TODO: implicit inferrance here, stripe => AUD as currency
        currency = 'AUD'
        _setup_accounts(currency, accounts)
        log.info(f"Booking {booking['booking_id']} is in type of stripe")
    elif booking['payment_type'] == 'usdt':
        currency = 'USDT'
        _setup_accounts(currency, accounts)
        log.info(f"Booking {booking['booking_id']} is in type of usdt")
    else:
        print('unknown type')
    
    referrer_uids = list(map(lambda m: m['uid'], referral_models))

    # fetch contact id [provider_xero_id, ...referral_xero_ids]
    contact_ids = get_contactId_from_account_numbers(
        [provider_model['uid']] + referrer_uids)
    
    if len(contact_ids) != len(referrer_uids) + 1:
        log.error(f"Accounting: booking {booking['booking_id']} cannot be created due to the missing of the contact {[i for i in (referrer_uids + [provider_model['uid']])  if i not in contact_ids]} ")
        return
    
    xero_provider_id = contact_ids[0]
    xero_referal_ids = contact_ids[slice(1, None)]

    booking_total = booking['total_fee_aud']
    platform_commission_gross = booking_total * provider_model['referral_config']['platform_commission']
    platform_commission = platform_commission_gross

    update_invoices_array = []

    # iterate referrer
    for idx, ref in enumerate(referral_models):
        reference_contribution = platform_commission_gross * ref['referral_config']['reward_layers'][idx]
        platform_commission -= reference_contribution
        r_line_item = LineItem(
            description=f"bookingId={booking['booking_id']}, contribution={reference_contribution}, tier={idx+1}",
            quantity=1.0,
            unit_amount=reference_contribution,
            # account code
            account_code=accounts['referral_commisssion'])

        log.info(f"generating updated invoice R{idx+1} reference referral_id={referrer_uids[idx]} for bookingid={booking['booking_id']} ")

        update_invoices_array.append(
            append_lineitems_to_primary_invoice(xero_referal_ids[idx], [r_line_item]))
        
        log.info(f"generated updated invoice R{idx+1} reference referral_id={referrer_uids[idx]} for bookingid={booking['booking_id']} ")

    #provider
    p_line_items = []
    p_line_item = LineItem(
        description=f"bookingId={booking['booking_id']}, total={booking_total}",
        quantity=1.0,
        unit_amount=booking_total,
        account_code=accounts['order_receive'])
    p_line_items.append(p_line_item)

    p_line_item = LineItem(
        description=f"bookingId={booking['booking_id']}, platform_commission={platform_commission}",
        quantity=1.0,
        unit_amount=-platform_commission,
        account_code=accounts['platform_commission'])
    p_line_items.append(p_line_item)
    
    p_line_item = LineItem(
        description=f"bookingId={booking['booking_id']}, referral_commission={platform_commission - platform_commission_gross}",
        quantity=1.0,
        unit_amount=platform_commission - platform_commission_gross,
        account_code=accounts['referral_reconciliation'])
    p_line_items.append(p_line_item)
    
    log.info(f"generating updated invoice provider_id={xero_provider_id} for bookingid={booking['booking_id']} ")

    update_invoices_array.append(
        append_lineitems_to_primary_invoice(xero_provider_id, p_line_items))

    log.info(f"generated updated invoice provider_id={xero_provider_id} for bookingid={booking['booking_id']} ")

    invoices = Invoices(invoices=update_invoices_array)
    try:
        api_response = api_instance.update_or_create_invoices(xero_tenant_id=tenant_id, invoices=invoices, summarize_errors=summarize_errors, unitdp=4)

        return api_response
    except AccountingBadRequestException as e:
        log.error("Accounting: Exception when calling AccountingApi->createBankTransactions: %s\n" % e)
        raise e

@xero_token_required
def create_contact_on_registration(uid: str):
    api_instance = AccountingApi(api_client)
    summarize_errors = 'True'
    contact = Contact(
        name = uid,
        account_number = uid)
    contacts = Contacts( 
        contacts = [contact])
    try:
        log.info(f"Accounting: Creating contact for account {uid}...")
        api_response = api_instance.create_contacts(tenant_id, contacts, summarize_errors)
        contacts = getvalue(api_response, 'contacts', '')

        log.info(f"Accounting: Contact for account {uid} created! Contact id is {contacts[0].contact_id}")
        return contacts[0]
    except AccountingBadRequestException and IndexError as e:
        log.error("Exception when calling AccountingApi->createContacts: %s\n" % e)
        raise e

@xero_token_required
def withdraw_request_received(
    account_id: str,
    amount: decimal.Decimal,
    currency_alias: str
):
    # important to setup accounts first
    _setup_accounts(currency_alias=currency_alias, accounts=accounts)


    api_instance = AccountingApi(api_client)

    balance = check_balance(account_id=account_id, currency_alias=currency_alias)
    now = datetime.now()
    delta = relativedelta(weeks=1)
    due_date = now + delta
    if balance - amount >= 0:
        contactIds = get_contactId_from_account_numbers(acc_nos=[account_id])
        if len(contactIds) == 0: 
            log.error(f"Accounting: contact with id: {account_id} cannot be found.")
            return
        contactId = contactIds[0]

        contact = Contact(
            contact_id=contactId)
        
        # use this ref number to identify specific bill in PRIMARY INVOICE line item.
        bill_ref = f"{account_id}_{datetime.now().strftime('%Y%m%d%H%M%S')}"

        # insert line item to existing primary invoice
        line_item = LineItem(
            description=f"bill_ref={bill_ref}",
            quantity=1.0,
            unit_amount=-amount,
            account_code=accounts['withdraw'])

        line_items = []
        line_items.append(line_item)
        
        primary_invoice = append_lineitems_to_primary_invoice(contact_id=contactId, line_items=line_items)

        # create bill
        bill_items = []
        bill_item = LineItem(
            description=f"bill_ref={bill_ref}",
            quantity=1.0,
            unit_amount=amount,
            account_code=accounts['withdraw'])
        bill_items.append(bill_item)
        bill = Invoice(
            type="ACCPAY",
            contact=contact,
            date=now,
            due_date=due_date,
            line_items=bill_items,
            reference=f"{accounts['currency_code'].name}_withdraw",
            status=TransactionStatusEnum.authorised)
        
        update_invoices = Invoices(
            invoices=[bill, primary_invoice])

        try:
            api_response = api_instance.update_or_create_invoices(
                xero_tenant_id=tenant_id, invoices=update_invoices, unitdp=4)

            return api_response
        except AccountingBadRequestException as e:
            log.error("Exception when calling AccountingApi->createInvoices: %s\n" % e)
            raise e
    else:
        raise PermissionError("No enough balance")

def check_balance(account_id: str, currency_alias: str) -> decimal.Decimal:
    balance = decimal.Decimal(0)

    # iterate all supported currencies
    for currency in xero_config['accounts']:
        if xero_config['accounts'][currency]['alias'] == currency_alias: 
            invoices = get_primary_invoice(account_id=account_id, currency_code=str(currency), detailed=False);

            if len(invoices) != 0:
                balance = invoices[0].amount_due

    return balance

"""
return object contain balance & booking txn details & withdraw invoice detail
{
    balance: Decimal,
    txns: [],
    withdraws: []
}
"""
def get_balance_with_txns_invoices(account_id: str) -> dict:
    result = {'balance': {}, 'txns': [], 'withdraws': []}
    # iterate all supported currencies
    for currency in xero_config['accounts']:
        currency_alias = xero_config['accounts'][currency]['alias']
        result['balance'][currency_alias] = decimal.Decimal(0)

        invoices = get_primary_invoice(account_id=account_id, currency_code=currency, detailed=True)
        if len(invoices) == 0: continue
        """
        bookings
        {
            booking_id: [item],
            booking_id2: [item]
        }
        """
        bookings = {}
        line_items = invoices[0].line_items
        result['balance'][currency_alias] = invoices[0].total

        
        for item in line_items:
            booking_id = get_booking_id(item.description)
            
            # withdraw line item
            if booking_id == None:
                account_name = get_account_name_by_code(item.account_code)
                if not 'WITHDRAW' in account_name.upper():
                    log.error(f"Invalid line item found in invoice {invoices[0].invoice_id}: \n {item}")
                    # result['withdraws'].append(item)
                
                continue

            item.date = get_booking_date(item.description)
            if booking_id not in bookings.keys():
                bookings[booking_id] = []
            bookings[booking_id].append(item)
        
        for booking in bookings.keys():
            booking_total = 0
            platform_commission = 0
            referral_reconciliation = 0
            order_receive_item = None
            for item in bookings[booking]:
                account_name = get_account_name_by_code(item.account_code)
                if 'REFERRAL COMMISSION' in account_name.upper():
                    item.currency_code = currency_alias
                    result['txns'].append(item)
                elif 'REFERRAL RECONCILIATION' in account_name.upper():
                    referral_reconciliation = item.line_amount
                elif 'ORDER RECEIVED' in account_name.upper():
                    booking_total = item.line_amount
                    item.currency_code = currency_alias
                    order_receive_item = item
                elif 'PLATFORM COMMISSION' in account_name.upper():
                    platform_commission = item.line_amount
            
            if order_receive_item != None:
                booking_total = booking_total + platform_commission + referral_reconciliation
                order_receive_item.line_amount = booking_total
                result['txns'].append(order_receive_item)

    bills = get_bills_by_username(account_id=account_id)
    result['withdraws'] = bills

    return result
    

def append_lineitems_to_primary_invoice(contact_id: str, line_items: [LineItem]):
    date_value = dateutil.parser.parse(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    due_date_value = dateutil.parser.parse(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    api_instance = AccountingApi(api_client)
    where = f'Reference="{accounts["currency_code"].name}_primary"'
    statuses = [ "AUTHORISED" ]
    order = 'Date Desc'
    contact_ids = [contact_id]
    # created_by_my_app = 'False'
    # summary_only = 'True'
    try:
        api_response = api_instance.get_invoices(xero_tenant_id=tenant_id,
                                                 where=where,
                                                 statuses=statuses,
                                                 page=0,
                                                 order=order,
                                                 contact_i_ds=contact_ids,
                                                 unitdp=4 )
        invoices = getvalue(api_response, "invoices", [])


        existing_invoice = None
        if invoices != None and len(invoices) != 0:
            existing_invoice = invoices[0]
        
        existing_line_items = getvalue(existing_invoice, 'line_items', [])
        existing_line_items.extend(line_items)


        r_contact = Contact(contact_id)

        if existing_invoice == None:
            invoice = Invoice(
                type="ACCREC",
                line_items=line_items,
                contact=r_contact,
                reference=f"{accounts['currency_code'].name}_primary", #currency code not alias
                status = "AUTHORISED",
                # currency_code=accounts['currency_code'],
                date = date_value,
                due_date = due_date_value,
            )
            return invoice
        else:
            existing_invoice.line_items = existing_line_items
            return existing_invoice

    except AccountingBadRequestException as e:
        log.error("Exception when calling AccountingApi->getInvoices: %s\n" % e)
        return None


@xero_token_required
def get_primary_invoice(account_id: str, currency_code: str, detailed: bool):
    api_instance = AccountingApi(api_client)
    where = f'Contact.Name="{account_id}" and Reference="{currency_code}_primary"'
    statuses = [ "AUTHORISED" ]
    order = 'Date Desc'
    # created_by_my_app = 'False'
    summary_only = 'True' if detailed else 'False'
    try:
        api_response = api_instance.get_invoices(xero_tenant_id=tenant_id,
                                                 where=where,
                                                 statuses=statuses,
                                                 page=0,
                                                 order=order,
                                                 unitdp=4)
        invoices = getvalue(api_response, "invoices", [])
        return invoices
    except AccountingBadRequestException as e:
        log.error(f"Exception when calling AccountingApi->getInvoices: {e}")


@xero_token_required
def get_bills_by_username(account_id: str):
    api_instance = AccountingApi(api_client)
    where = f'Contact.Name="{account_id}" and type="ACCPAY"'
    order = 'Date Desc'
    statuses = [ "AUTHORISED", "PAID", "VOIDED"]
    # created_by_my_app = 'False'
    # summary_only = 'True'

    try:
        api_response = api_instance.get_invoices(xero_tenant_id=tenant_id,
                                                 where=where,
                                                 page=0,
                                                 statuses=statuses,
                                                 order=order,
                                                 unitdp=4 )
        return getvalue(api_response, "invoices", "")
    except AccountingBadRequestException as e:
        log.error("Exception when calling AccountingApi->getInvoices: %s\n" % e)
        return []

@xero_token_required
def get_txns(account_id: str):
    api_instance = AccountingApi(api_client)
    where = f'Type=="RECEIVE" AND Contact.Name=="{account_id}" AND Status=="AUTHORISED"'
    order = 'Date Desc'
    if_before = dateutil.parser.parse("2020-02-06T12:17:43.202-08:00")
    try:
        api_response = api_instance.get_bank_transactions(
            xero_tenant_id=tenant_id, if_modified_since=if_before, where=where, order=order, unitdp=4)
        txns = getvalue(api_response, 'bank_transactions', '')
        return txns
    except AccountingBadRequestException as e:
        log.error("Exception when calling AccountingApi->getBankTransactions: %s\n" % e)
        return []

@xero_token_required
def get_contactId_from_account_numbers(acc_nos: list):
    api_instance = AccountingApi(api_client)
    where = 'ContactStatus=="ACTIVE" AND '
    for id, acc in enumerate(acc_nos):
        if id != len(acc_nos)-1:
            where += 'AccountNumber=="' + acc + '" OR '
        else:
            where += 'AccountNumber=="' + acc + '"'

    order = 'Name ASC'
    include_archived = 'False'
    summary_only = 'True'

    try:
        api_response = api_instance.get_contacts(xero_tenant_id=tenant_id, where=where,
                                                 order=order, include_archived=include_archived, summary_only=summary_only)
        resp = getvalue(api_response, 'contacts', '')
        # sort response contact detail in original order
        result = []
        for acc in acc_nos:
            present = False
            for r in resp:
                if r.account_number == acc:
                    present = True
                    result.append(r.contact_id)
                    break
            if not present:
                log.info(f"Accounting: contact: {acc} is not present.")
                contact = create_contact_on_registration(acc)
                result.append(contact.contact_id)

        return result
    except AccountingBadRequestException as e:
        log.error("Exception when calling AccountingApi->getContacts: %s\n" % e)

def get_accountId_by_wallet(wallet: str):
    return;

# create currency code
@xero_token_required
async def _create_currency_code():
    api_instance = AccountingApi(api_client)

    for c in xero_config["currencies"]:
        currency = Currency(
            code=CurrencyCode[c['code']],
            description=c['description'])
        try:
            api_response = api_instance.create_currency(tenant_id, currency)
        except AccountingBadRequestException as e:
            if e.status == 400:
                print("Currency exist, ignore")
                continue
            print("Exception when calling AccountingApi->createCurrency: %s\n" % e)
            raise e


# create accounting account
@xero_token_required
async def _create_accounting_accounts():

    api_instance = AccountingApi(api_client)
    for currency in list(xero_config['accounts']):
        for acc in xero_config['accounts'][currency]['list']:
            account = Account(
                code=acc['code'],
                name=acc['name'],
                type=AccountType[acc['type']],
                description=acc['description'],
                tax_type=acc['tax_type'])
            try:
                api_response = api_instance.create_account(tenant_id, account)
            except AccountingBadRequestException as e:
                if e.status == 400:
                    print(f"Account {acc['code']} exist, ignore")
                    continue
                print("Exception when calling AccountingApi->createAccount: %s\n" % e)
                raise e

async def xero_health_check():
    try:
        log.error(f"Checking xero connection with client_id: {client_id} & client_secret: {client_secret}...")
        # await _create_currency_code()
        await _create_accounting_accounts()
    except Exception as ex:
        log.error(f"Fatal exception occurred during checking xero connection. Failed to create app. \n {ex}")
        pass
    
"""
alias: currency alias, USDT/AUD
accounts: the accounts correlated with the given current
"""
def _setup_accounts(currency_alias: str, accounts: dict):
    accounts_for_currency = []
    for account_type in xero_config['accounts']:
        if xero_config['accounts'][account_type]['alias'].upper() == currency_alias.upper():
            accounts_for_currency = xero_config['accounts'][account_type]['list']
            accounts['currency_code'] = CurrencyCode(account_type)

    for account in accounts_for_currency:
        if 'ORDER' in account['name'].upper():
            accounts['order_receive'] = account['code']
        elif 'PLATFORM' in account['name'].upper():
            accounts['platform_commission'] = account['code']
        elif 'REFERRAL COMMISSION' in account['name'].upper():
            accounts['referral_commisssion'] = account['code']
        elif 'WITHDRAW' in account['name'].upper():
            accounts['withdraw'] = account['code']
        elif 'REFERRAL RECONCILIATION' in account['name'].upper():
            accounts['referral_reconciliation'] = account['code']

def get_account_name_by_code(account_code: str):
    for account_type in xero_config['accounts']:
        for acc in xero_config['accounts'][account_type]['list']:
            if str(acc['code']) == account_code:
                return acc['name']
    return ''
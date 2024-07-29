import os
import logging
import json
from inspect import getmembers, isclass
import asyncio
from enum import Enum
from pydantic_settings import BaseSettings

from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError

from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.security import HTTPBearer, OAuth2PasswordBearer
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

from bdating_common.model import BookingStatus, HealthResponse, ConsumerProfile, MultiLangEnum, WithdrawModel
from bdating_common import model as model_module
# from bdating_common import model_zh as model_zh_module
# from bdating_common import model_en as model_en_module
# from bdating_common import xero_helper, xero_utils

from bdating_common.auth0_token_helper import IllegalTokenExcpetion, Auth0TokenVerifier
from fastapi.responses import JSONResponse
from bdating_common.es_helper import es_get_result_to_dict, es_search_result_to_dict
from fastapi import WebSocket
from fastapi.websockets import WebSocket, WebSocketDisconnect
import redis
import aioredis
from aioredis.pubsub import Channel
from auth0.v3.authentication import Users as Auth0Users
from typing import Union, Any, Dict, Optional

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

log = logging.getLogger(__name__)


def get_model_enum_values():
    model_enums = {}
    for name, member in getmembers(model_module, isclass):
        if issubclass(member, MultiLangEnum) and member is not MultiLangEnum:
            try:
                trans = member.translates()
                res = []
                for key in member:
                    _d = {'_key': key}
                    for lang in ('en', 'zh'):
                        # if the given key is not need to be translated
                        if key not in trans:
                            _d[lang] = key.replace('_', ' ').capitalize()
                        else:
                            _d[lang] = trans[key].get(lang)
                            if _d[lang] is None:
                                _d[lang] = key.replace('_', ' ').capitalize()
                    res.append(_d)
                model_enums[name] = res
            except (AttributeError, KeyError) as ex:
                log.warning('Enum %s has no proper translation defined', name)
                res = []
                for m in member.__members__:
                    res.append({'_key': m, 'en': m.replace(
                        '_', ' ').capitalize(), 'zh': m.replace('_', ' ').capitalize()})
                model_enums[name] = res
    return model_enums


#def get_model_enum_values2():
#    model_enums = {}
#    for data_type_name in dir(model_module):
#        if not data_type_name.startswith('__') and data_type_name != 'Enum' and type(model_module.__dict__[data_type_name]) == enum.EnumMeta:
#            model_enums[data_type_name] = [
#                {
#                    '_key': variable_name,
#                    'en': model_en_module.__dict__[data_type_name].__dict__[variable_name].value,
#                    'zh': model_zh_module.__dict__[data_type_name].__dict__[variable_name].value,
#                }
#                for variable_name in dir(model_module.__dict__[data_type_name]) if not variable_name.startswith('__')
#            ]
#    return model_enums


class Settings(BaseSettings):
    app_name: str = 'StandardBdatingAPI'
    app_namespace: str = os.getenv('NAMESPACE', "")
    admin_email: str = "admin@bdating.io"
    app_type: str = 'consumer'
    es_endpoint: str = os.getenv('ELASTICSEARCH_HOSTS')
    es_index: str = 'bdating'
    auth0_namespace: str = 'https://app.bdating.io/'
    redis_host: str = os.getenv('REDIS_HOST')
    redis_port: int = 6379
    redis_password: Optional[str] = os.getenv('REDIS_PASSWORD')
    cors_origins: str = os.getenv('CORS_ORIGINS', 'http://localhost:3000')
    token_cache_db_id: int = 0
    lock_db_id: int = 1
    in_app_notif_cache_id: int = 2


settings = Settings()
token_auth_scheme = HTTPBearer()
token_verifier = Auth0TokenVerifier()

token_cache_redis = None  # TODO rework the global clients.


def _get_token_payload(token: str) -> str:
    global token_cache_redis
    if settings.redis_host:
        if token_cache_redis is None:
            token_cache_redis = redis.Redis(
                settings.redis_host, settings.redis_port,
                db=settings.token_cache_db_id,
                password=settings.redis_password
            )
        cached_value = token_cache_redis.get(token)
        if cached_value is not None:
            return cached_value.decode('utf-8')
    try:
        payload = token_verifier.verify(token)
        if payload.get("status") == 'error':
            log.warn('Payload status == error payload: %s, token: %s', payload, token, exc_info=True)
            raise IllegalTokenExcpetion()
        payload_str = json.dumps(payload, default=str)
        if token_cache_redis is not None and payload:
            ttl = 86400 * 1000  # hard code 1 day, ttl value is in milliseconds
            token_cache_redis.setex(
                token, ttl, payload_str)
        return payload_str
    except Exception as e:
        log.warn('Token verification failed', exc_info=True)
        raise IllegalTokenExcpetion(e)


def _get_uid(token: str):
    payload_str = _get_token_payload(token)
    return json.loads(payload_str).get(f"{settings.auth0_namespace}uid")


def _get_sub(token: str):
    payload_str = _get_token_payload(token)
    return json.loads(payload_str).get(f"sub")

def get_uid(token: str, token_verifier: object):
    global token_cache_redis
    if settings.redis_host:
        if token_cache_redis is None:
            token_cache_redis = redis.Redis(
                settings.redis_host, settings.redis_port,
                db=settings.token_cache_db_id,
                password=settings.redis_password
            )
        cached_value = token_cache_redis.get(token.credentials)
        if cached_value is not None:
            return json.loads(cached_value.decode('utf-8')).get(f"{settings.auth0_namespace}uid")
    try:
        result = token_verifier.verify(token.credentials)
        log.warn('result %s', result)
        if result.get("status") == 'error':
            raise IllegalTokenExcpetion()
        domain = os.environ.get('DOMAIN')
        log.warn('domain %s', domain)
        users = Auth0Users(domain)
        userinfo = users.userinfo(token.credentials)
        log.warn('userinfo %s', userinfo)
        uid = userinfo.get(f"{settings.auth0_namespace}uid")
        # value = result.get(f"{settings.auth0_namespace}uid")
        # log.warn('uid retrieved is %s', value)
        if token_cache_redis is not None and uid:
            ttl = 86400 * 1000  # hard code 1 day, ttl value is in milliseconds
            token_cache_redis.setex(
                token, ttl, json.dumps(payload, default=str))
        return uid
    except Exception as e:
        log.warn('Token verification failed', exc_info=True)
        raise IllegalTokenExcpetion(e)


def get_contact(token: str):
    try:
        payload = token_verifier.verify(token)
        if payload.get('status') == 'error':
            raise IllegalTokenExcpetion()
        contact = payload.get(f"{settings.auth0_namespace}name")
        return contact
    except Exception as e:
        log.warn('Token verification failed', exc_info=True)
        raise IllegalTokenExcpetion(e)


async def ws_reader(channel: Channel, ws: WebSocket):
    while await channel.wait_message():
        text = None
        try:
            text = (await channel.get()).decode('utf-8')
            msg = json.loads(text)
            await ws.send_text(json.dumps({**msg, "channel": channel.name.decode('utf-8')}, default=str))
        except Exception as e:
            log.error(
                'Could not process channel mesage from %s. Message: %s. Error: e', channel.name, text, e)


async def redis_connector(
    websocket: WebSocket, uid: str
):
    async def consumer_handler(ws: WebSocket, redis_client: object):
        try:
            if uid:
                own_channel = (await redis_client.subscribe(uid))[0]
                log.info('web client ws subscribed: %s ', uid)
                asyncio.create_task(ws_reader(own_channel, ws))
            additional_channel = None
            while True:
                message = await ws.receive_text()
                log.info('web client message: %s ', message)
                message = message.strip()
                if message.lower() == "close":
                    await websocket.close()
                    break
                else:
                    if additional_channel:
                        redis_client.unsubscribe(additional_channel)
                    additional_channel = (await redis_client.subscribe(message))[0]
                    log.info('web client ws subscribed: %s ', message)
                    asyncio.create_task(ws_reader(additional_channel, ws))
        except WebSocketDisconnect:
            log.debug("Socket disconnected, no big deal")

    redis = await aioredis.create_redis_pool(
        address=f"redis://{settings.redis_host}:{settings.redis_port}",
        db=settings.in_app_notif_cache_id,
        password=settings.redis_password
    )
    consumer_task = consumer_handler(websocket, redis)
    done, pending = await asyncio.wait(
        [consumer_task, ], return_when=asyncio.FIRST_COMPLETED,
    )
    log.debug(f"Done task: {done}")
    for task in pending:
        log.warning(f"Canceling task: {task}")
        task.cancel()
    redis.close()
    await redis.wait_closed()


async def calculate_referral_incomes(es, account_id: str):
    """
    return aggregated referral incomes data by currency
    e.g.
    {
        "UDST" : 40,
        "BDC": 20
    }
    return {} if no referral txn match the account id is found
    """
    log.warning(f"Calculating referral incomes for account id: {account_id}")
    query = {
        '_source':['referral_amount', 'referral_currency', 'booking.provider_uid', 'booking.consumer_uid', 'timestamp'], # Return these fields only
        "query": {
            "bool": {
                "must": [
                    {
                        "match": {
                            "type": "referral_txn_history"
                        }
                    },
                    {
                        "match": {
                            "referral_uid": account_id
                        }
                    }
                ]
            }
        }
    }
    resp = await es.search(body=query)
    if resp == None or resp['size'] == 0:
        return {}
    
    aggs = {}
    for i in resp['results']:
        if i['referral_currency'] not in aggs.keys():
            aggs[i['referral_currency']] = i['referral_amount']
        else:
            aggs[i['referral_currency']] += i['referral_amount']

    return aggs

async def list_referral_incomes(es, account_id: str):
    log.warning(f"listing referral incomes for account id: {account_id}")
    query = {
        '_source':['referral_amount', 'referral_currency', 'booking.provider_uid', 'booking.consumer_uid', 'timestamp'], # Return these fields only
        "query": {
            "bool": {
                "must": [
                    {
                        "match": {
                            "type": "referral_txn_history"
                        }
                    },
                    {
                        "match": {
                            "referral_uid": account_id
                        }
                    }
                ]
            }
        }
    }
    resp = await es.search(body=query)
    return resp['results']

async def get_my_booking_incomes(es, account_id: str):
    log.warning(f"Calculating booking incomes for account id: {account_id}")
    query = {
        '_source':['payment_amount', 'payment_method', 'timestamp', 'provider_uid', 'consumer_uid'], # Return these fields only
        "query": {
            "bool": {
                "must": [
                    {
                        "match": {
                            "type": "booking"
                        }
                    },
                    {
                        "match": {
                            "status": BookingStatus.fulfilled
                        }
                    },
                    {
                        "match": {
                            "provider_uid": account_id
                        }
                    }
                ]
            }
        }
    }
    result = await es.search(body=query)

    if result == None or result['size'] == 0:
        return {
            'bookings': [],
            'aggs': {}
        }
    
    aggs = {}
    for i in result['results']:
        key = i['payment_method']
        if key not in aggs.keys():
            aggs[key] = i['payment_amount']
        else:
            aggs[key] += i['payment_amount']

    resp = {
        'bookings': result['results'],
        'aggs': aggs 
    }

    return resp

def create_app():
    app = FastAPI(title=settings.app_name)
    es = Elasticsearch(settings.es_endpoint)


    @ app.get("/health", response_model=HealthResponse)
    def get_health():
        return {"status": "OK"}

    @app.exception_handler(NotFoundError)
    async def es_not_found_handler(request, exc):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=jsonable_encoder({"detail": "Not found"}),)

    @app.exception_handler(IllegalTokenExcpetion)
    async def illegal_Auth0_token_exception_handler(request, exc):
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content=jsonable_encoder({"detail": "Illegal token"}),)

    @app.get("/me")
    def get_own_profile_info(token: str = Depends(token_auth_scheme)):
        """
        Find this user's own profile info.
        """
        uid = get_uid(token, token_verifier)
        return es_search_result_to_dict(es.get(index=settings.es_index, id=f"{uid}:{settings.app_type}"))

    @app.patch("/me")
    def update_own_profile_info(profile: ConsumerProfile, token: str = Depends(token_auth_scheme)):
        """
        Update the profile for the user.
        If the profile does not exist, create it in the first place.
        """

        profile = jsonable_encoder(profile)
        log.debug('profile %s', profile)
        log.debug('token %s', token)
        uid = get_uid(token, token_verifier)
        return {}
        return es.update(index=settings.es_index, id=f"{uid}:{settings.app_type}", doc_as_upsert=True, doc=profile)

    @app.get('/config/app')
    def get_app_config():
        """get application default configuration"""
        result = {
            'enum_values': get_model_enum_values()
        }
        return result
    
    # @app.get('/incomes/my')
    def get_my_incomes(
        token: str = Depends(token_auth_scheme)
    ):
        uid = get_uid(token, token_verifier)
        # balance_bundle = xero_helper.get_balance_with_txns_invoices(account_id=uid)
        
        # txns = balance_bundle['txns']
        # booking_orders = []
        # referral_orders = []
        # withdraws = []
        # for txn in txns:
        #     account_name = xero_helper.get_account_name_by_code(txn.account_code)
        #     if 'REFERRAL COMMISSION' in account_name.upper():
        #         item = _map_xero_txn_to_resp_item(es= es, txn=txn)
        #         referral_orders.append(item)
        #     elif 'ORDER RECEIVED' in account_name.upper():
        #         item = _map_xero_txn_to_resp_item(es= es, txn=txn)
        #         booking_orders.append(item)
        # # withdraws = balance_bundle['withdraws']

        # withdraws = list(map( lambda invoice: { 'invoice_id': invoice.invoice_id, 'amount': invoice.total, 'currency': invoice.currency_code, 'date': invoice.date, 'status': invoice.status }, balance_bundle['withdraws']))
    
        return {
            # 'aggs': balance_bundle['balance'],
            # 'bookings': booking_orders,
            # 'referrals': referral_orders,
            # 'withdraws': withdraws
            'aggs': 0,
            'bookings': [],
            'referrals': [],
            'withdraws': []
        }

    @app.post('/incomes/withdraw')
    def request_withdraw(payload: WithdrawModel, token: str = Depends(token_auth_scheme)):
        uid = get_uid(token, token_verifier)
        # try:
        #     xero_helper.withdraw_request_received(account_id=uid, amount=payload.amount, currency_alias=payload.currency)
        #     return f"Withdraw request for amount {payload.amount} {payload.currency} submitted."
        # except PermissionError as e:
        #     log.info(e)
        #     raise HTTPException(401, f"Error {e} when withdrawing {payload.amount} {payload.currency}.")
        # except Exception as ex:
        #     log.error(ex)
        #     raise HTTPException(500, f"Unexpected error when withdrawing {payload.amount} {payload.currency}.")

    if settings.cors_origins:
        origins = settings.cors_origins.split(',')
        app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
            max_age=7200
        )
    return app


class PublishAction(Enum):
    message = 'message'
    data = 'data'
    action = 'action'


def publish_message(message: Union[Dict[Any, Any], str], uid: str, sync_redis: object = None):
    """Publish a message to a user identified by uid
    mesage format: 
    {
        "channel": "xxxx", # what channel this message was broadcasted to. Only clients subscribed to this channel can receive this message. Yet as one client may subscribe to multiple channels, this field is kept to notify which channel this is about.
        "type:": "message|data|action", 
        # when type is data, means the user (uid is defined by channel) had related data change.
        # when type is message, means the system want some infromation displayed in real time on the user's app if the user is online. Body is fixed format { "message": message }
        # when type is action, ...we havent' decided what to do.
        "body": {
        } # the message body. 
            # for message type, body is like { "message": message }
            # for data type, body is like {"slot_update": ["slot_ids"]} / {"slot_locked": ["slot_ids"]} /{"booking_fulfilled": ["booking_id"]} etc.
            # for action type, body is not defined yet.
        }

    The caller has to put message like 
    publish_message(dict(
        action=PublishAction.data.name,
        body={...}
        ), uid=user_id)

    or if simply just push a text message
    publish_message("Please display this to the user", uid=user_id)

    """
    if not sync_redis:
        sync_redis = redis.Redis(
            host=settings.redis_host,
            port=settings.redis_port,
            db=settings.in_app_notif_cache_id,
            password=settings.redis_password,
        )
    if isinstance(message, Dict):
        sync_redis.publish(uid, json.dumps(message, default=str))
        # log.debug(
        #     f"--- api_common.py:publish_message(): uid={uid}, message={json.dumps(message, default=str)}")
    else:
        sync_redis.publish(uid, json.dumps({
            "type": "message",
            "body": {"message": message}
        }))

        # log.debug("--- api_common.py:publish_message(): published message: ", message)

def _map_xero_txn_to_resp_item(es, txn):
    booking_fallback = {
        'consumer_uid': 'Unknown',
        'provider_uid': 'Unknown',
        'date': txn.date,
        'payment_method': txn.currency_code,
        'payment_amount': txn.line_amount
    }
    booking_id = xero_utils.get_booking_id(txn.description)
    
    if booking_id != None:
        query = {
            '_source':['provider_uid', 'consumer_uid', 'timestamp'], # Return these fields only
            "query": {
                "bool": {
                    "must": [
                        {
                            "match": {
                                "type": "booking"
                            }
                        },
                        {
                            "match": {
                                "booking_id": booking_id
                            }
                        }
                    ]
                }
            }
        }
        result = es_search_result_to_dict(es.search(index=settings.es_index, body=query))
        if len(result['results']) == 0:
            log.warn(f"In line item id={txn.line_item_id}, booking with booking_id={booking_id} can't be found")
            
            return booking_fallback
        else:
            booking = result['results'][0]
            # xero is the source of trust of payment currency & amount
            booking['payment_method'] = txn.currency_code
            booking['payment_amount'] = txn.line_amount
            booking['date'] = txn.date

            return booking
    else:
        log.warn(f"In line item id={txn.line_item_id}, no booking id found")
        return booking_fallback

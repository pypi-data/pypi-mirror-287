import os
import stripe
import logging
log = logging.getLogger(__name__)
import requests
def create_stripe_payment_intent(
        amount: float, 
        booking_id: str,
        currency: str = "AUD",
    ):
    try:
        payment_intent = stripe.PaymentIntent.create(
            api_key=os.environ['STRIPE_API_KEY'],
            amount=int(amount*100),
            currency=currency,
            payment_method_types=[ x.strip() for x in os.getenv(
                'STRIPE_PAYMENT_METHODS','card').split(',') ],
            # payment_method_types=['card'], # TODO add more payment methods
            description="payment for booking: " + booking_id,
            metadata={
                "booking_id": booking_id
            },
        )
        return {"StripeClientSecret": payment_intent["client_secret"], 'id': payment_intent['id']}
    except Exception as e:
        log.error("STstripeRIPE: error when creating payment, %s", e)
        raise e
def cancel_stripe_payment_intent(
        payment_intent_id: str,
    ):
    log.info('cancel_stripe_payment_intent %s', payment_intent_id)
    try:
        # wth : python does not have a clear way to cancel by id
        # doc: https://stripe.com/docs/api/payment_intents/cancel
        payment_intent = requests.post(
            url=f"https://api.stripe.com/v1/payment_intents/{payment_intent_id}/cancel",
            auth=(os.environ['STRIPE_API_KEY'], '')
        ).json()
        log.debug('cancel_stripe_payment_intent %s', payment_intent)
        return {"status": payment_intent["status"]}
    except Exception as e:
        log.error("stripe: error when cancelling payment, %s", e)
        raise e
def chech_stripe_payment_intent_payed(
        payment_intent_id: str,
    ):
    try:
        payment_intent = stripe.PaymentIntent.retrieve(
            api_key=os.environ['STRIPE_API_KEY'],
            id=payment_intent_id,
        )
        return {"status": payment_intent["status"]}
    except Exception as e:
        log.error("stripe: error when check payment, %s", e)
        raise e
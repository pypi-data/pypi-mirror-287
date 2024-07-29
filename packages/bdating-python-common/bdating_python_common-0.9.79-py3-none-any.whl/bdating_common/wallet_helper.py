import os
import requests


def get_matched_bdating_wallet_info(booking_id: str):
    endpoint = os.environ['BDATING_WALLET_API_ENDPOINT']
    endpoint_key = os.environ['BDATING_WALLET_API_KEY']
    return requests.get(
        url=f"{endpoint}find_match",
        params={
            'tid': booking_id
        },
        headers={
            "x-api-key": endpoint_key
        }
    ).json()


def release_wallet_by_booking_id(booking_id: str):
    endpoint = os.environ['BDATING_WALLET_API_ENDPOINT']
    endpoint_key = os.environ['BDATING_WALLET_API_KEY']
    return requests.get(
        url=f"{endpoint}release",
        params={
            'tid': booking_id
        },
        headers={
            "x-api-key": endpoint_key
        }
    ).json()

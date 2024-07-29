import logging


log = logging.getLogger(__name__)

def description_to_dict(description: str):
    try:
        pairs = [item.split('=') for item in description.split(',')]

        # create a dictionary from pairs
        return {key.strip(): value.strip() for key, value in pairs}
    except Exception as e:
        log.error(f"Xero exception catched when parsing {description} error == {e}")
        return {}


def get_booking_id(description: str):
    dict = description_to_dict(description)
    booking_id = None
    try:
        booking_id = dict['bookingId']
    except KeyError as e:
        pass
    return booking_id


def get_booking_date(description: str):
    dict = description_to_dict(description)
    date = None
    try:
        booking_id = dict['bookingId']
        date = booking_id.split(":")[-1][:8]
    except KeyError and IndexError as e:
        pass
    return int(date)
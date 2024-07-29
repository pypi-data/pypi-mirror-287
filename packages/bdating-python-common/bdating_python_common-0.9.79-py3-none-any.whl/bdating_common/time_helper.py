import logging
from typing import Tuple
from datetime import datetime
import calendar
import math

log = logging.getLogger(__name__)
MIN_SLOT_IN_DAY = 0
MAX_SLOT_IN_DAY = 47



def parse_slot(slot_id: int) -> Tuple[datetime, int]:

    try:
        slot = slot_id % 100
        if slot < MIN_SLOT_IN_DAY or slot > MAX_SLOT_IN_DAY:
            return None, None
        return datetime(slot_id // 1000000, slot_id // 10000 % 100, slot_id // 100 % 100), slot
    except ValueError:
        return None, None


def convert_slot_to_epoch(slot_id: int) -> int:
    date_time, _ = parse_slot(slot_id=slot_id)
    return int(date_time.timestamp()) + slot_id % 100 * 30 * 60


def convert_slot_to_date_time_str(slot_id: int) -> str:
    try:
        slot_id=str(slot_id)
        year = slot_id[0:4]
        month = slot_id[4:6]
        day = slot_id[6:8]
        slotIndex = slot_id[8:10]
        hour = str( int(math.floor(int(slotIndex)) / 2)).zfill(2)
        minutes = str((int(slotIndex) % 2) * 30).zfill(2)
        time = "%s-%s-%s %s:%s" % (day,calendar.month_abbr[int(month)], year, hour, minutes)
        return time
    except Exception as ex:
        print(ex)
        return ""
        

if __name__ == "__main__":
    print(convert_slot_to_epoch(2022010123))
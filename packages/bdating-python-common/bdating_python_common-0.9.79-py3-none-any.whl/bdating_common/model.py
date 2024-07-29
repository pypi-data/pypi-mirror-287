import os
from typing import Optional
from pydantic import BaseModel
from enum import Enum
import decimal

import yaml

# data model

DIR, _ = os.path.split(os.path.abspath(__file__))
with open(os.path.join(DIR, 'enum_translation.yml')) as f:
    trans_data = yaml.safe_load(f)

class Location(BaseModel):
    lat: float
    lon: float

class Rating(BaseModel):
    avg_rating: float
    avg_on_time: float
    avg_service: float
    avg_accurate_profile_description: float


class BaseProfile(BaseModel):
    uid: Optional[str]
    name: str = ""
    referrer: Optional[str] = ""
    gender: str = ""
    register_timestamp: int = 0


class MultiLangEnum(str, Enum):
    @classmethod
    def translates(cls):
        return trans_data[cls.__name__]

class Gender(MultiLangEnum):
    male = 'male'
    female = 'female'

class EyeColor(MultiLangEnum):
    blue = 'blue'
    black = 'black'
    brown = 'brown'
    green = 'green'
    other = 'other'

class HairColor(MultiLangEnum):
    blue = 'blue'
    black = 'black'
    blond = 'blond'
    red = 'red'
    ash_blonde = 'ash_blonde'
    pink = 'pink'
    purple = 'purple'
    brunette = 'brunette'
    other = 'other'

class Ethnicity(MultiLangEnum):
    asian = 'asian'
    african = 'african'
    latin_american = 'latin_american'
    caucasian = 'caucasian'
    hispanic = 'hispanic'
    middle_eastern = 'middle_eastern'

class Build(MultiLangEnum):
    athletic = 'athletic'
    chunky = 'chunky'
    fit = 'fit'
    slender = 'slender'
    skinny = 'skinny'
    busty = 'busty'
    curvy = 'curvy'
    voluptuous = 'voluptuous'

class Bust(MultiLangEnum):
    a = 'a'
    b = 'b'
    c = 'c'
    d = 'd'
    e = 'e'
    f = 'f'
    g_plus = 'g_plus'


class DressSize(MultiLangEnum):
    six = 'six'
    eight = 'eight'
    ten = 'ten'
    twelve = 'twelve'
    fourteen = 'fourteen'
    fourteen_plus = 'fourteen_plus'

class SpeakingLanguage (MultiLangEnum):
    english = 'english'
    mandarin = 'mandarin'
    japanese = 'japanese'
    korean = 'korean'
    cantonese = 'cantonese'
    romanian = 'romanian'
    fijian = 'fijian'
    russian = 'russian'
    french = 'french'
    italian = 'italian'
    spanish = 'spanish'
    arabic = 'arabic'

class PaymentMethod (MultiLangEnum):
    usdt = 'usdt'
    # card = 'card'
    cash = 'cash'

class TimeSlotStatus(MultiLangEnum):
    available = 'available'
    attempt = 'attempt'
    pending_payment = 'pending_payment'
    booked = 'booked'
    locked = 'locked'


class BookingStatus(MultiLangEnum):
    attempt = 'attempt'
    pending_payment = 'pending_payment'
    archived = 'archived'
    confirmed = 'confirmed'
    cancel_attempt = 'cancel_attempt'
    canceled = 'canceled'
    fulfilled = 'fulfilled'
    deleted = 'deleted'  # need this? or simply delete it. as _id will conflict
    expire_payment = 'expire_payment'


class ProviderProfile(BaseProfile):
    address: str
    postcode: Optional[int] = None
    city: Optional[str] = None
    country: Optional[str] = None
    age: int = 27
    location: Location
    contact_detail: Optional[str] = ""
    rate_aud: Optional[int] = 150
    hair_color: Optional[HairColor] = None
    build: Optional[Build] = None
    ethnicity: Optional[Ethnicity] = None
    eye_color: Optional[EyeColor] = None
    bio: Optional[str] = None
    photos: list[str] = []
    height: Optional[int] = None
    bust: Optional[Bust] = None
    avg_on_time: Optional[float] = None
    avg_service: Optional[float] = None
    avg_rating: Optional[float] = None
    avg_accurate_profile_description: Optional[float] = None
    dress_size: Optional[DressSize] = None
    speaking_language: list[SpeakingLanguage] = []
    payment: Optional[list[PaymentMethod]] = []
    instruction_images: Optional[list[str]] = []
    instruction_text: Optional[str] = None
    email: Optional[str] = None


class ConsumerProfile(BaseProfile):
    contact: str = None
    name: str = None
    referrer: str = None
    email: str = None

class TimeSlot(ProviderProfile):
    slot_id: int  # the slot id, YYYYmmddXX
    slot_status: TimeSlotStatus = TimeSlotStatus.available


# details of a booking, which is shown to the provider and consumer
class BookingDetail(TimeSlot):
    total_fee_aud: int


class BookingHistory(BaseModel):  # state chagen history of a booking
    ationer: str
    timestamp: int
    additional_comment: Optional[str]


class Booking(BaseModel):  # booking to a timeslot
    consumer_uid: str
    provider_uid: str
    all_slots: list[int] = []
    status: BookingStatus
    consumer_comments: Optional[str]
    consumer_rating: Optional[float]
    provider_comments: Optional[str]
    provider_rating: Optional[float]
    last_update: int
    detail: BookingDetail
    bdating_wallet: str = ''
    total_fee_aud: int
    book_time: int  # epoch second of booked
    history: list[BookingHistory] = []


class Transaction(BaseModel):
    consumer_uid: str
    provider_uid: str
    booking: Booking
    timestamp: int
    total_fee_aud: int


# response model


class SingleProviderResponse(ProviderProfile):
    pass


class SingleConsumerResponse(ConsumerProfile):
    pass


class SingleTimeSlotResponse(TimeSlot):
    pass


class SingleBookingResponse(Booking):
    pass


class SingleTransactionResponse(Transaction):
    pass


class ProviderListResponse(BaseProfile):
    results: list[ProviderProfile] = []
    start: Optional[int]
    total_size: Optional[int]
    next_cursor: Optional[str]


class TimeSlotListResponse(BaseProfile):
    results: list[TimeSlot] = []
    start: Optional[int]
    total_size: Optional[int]
    next_cursor: Optional[str]


class BookingListResponse(BaseProfile):
    results: list[Booking] = []
    start: Optional[int]
    total_size: Optional[int]
    next_cursor: Optional[str]


class OrderListResponse(BaseProfile):
    results: list[Booking] = []
    start: Optional[int]
    total_size: Optional[int]
    next_cursor: Optional[str]

# general model


class HealthResponse(BaseModel):
    status: str

class NotificationsModel(BaseModel):
    notifications: list[str] = []

class ReferralConfig(BaseModel):
    platform_commission: float
    reward_layers: list[float]

class RefAndCommissionModel(BaseModel):
    uid: str
    referral_config: ReferralConfig

class InvoiceStatusEnum(str, Enum):
    authorised = 'AUTHORISED'
    paid = 'PAID'
    voided = 'VOIDED'

class TransactionStatusEnum(str, Enum):
    authorised = 'AUTHORISED'

class WithdrawModel(BaseModel):
    currency: str
    amount: decimal.Decimal
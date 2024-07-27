from typing import List
from pydantic import BaseModel, Field


class PostSignInRequest(BaseModel):
    remember_me: bool = Field(False, alias="rememberMe")
    email: str
    password: str


class PostSignInResponse(BaseModel):
    class Data(BaseModel):
        access: str = Field(alias="Access")
        refresh: str = Field(alias="Refresh")

    data: Data


class GetActiveOffersParams(BaseModel):
    fiat: str
    crypto: str
    banks: str
    amount: str
    type: str
    page: int
    limit: int
    sort: str


class GetActiveOffersResponse(BaseModel):
    class Info(BaseModel):
        class Offer(BaseModel):
            class PaymentMethod(BaseModel):
                crypto_id: int
                card: str
                id: str
                num_id: int
                token: str
                tech: str

            payment_method: List[PaymentMethod] = Field(alias='paymentMethod')
            country_code: str = Field(alias='countryCode')
            description: str
            create_time: str
            internal_id: str
            external_id: str
            liquidity_fiat: float
            liquidity_crypto: float
            limit_min: float
            limit_max: float
            course: float
            therms: str
            status: str
            crypto_token: str
            expire_offer_time: str
            need_merchant: bool
            origin: str
            is_grey: bool
            crypto_market: str
            type: str
            is_fixed: bool
            pro: bool
            income: str
            bonus: str

        class User(BaseModel):
            client_id: int
            nickname: str
            email: str
            avatar: str
            is_blocked: bool
            is_verified: bool = Field(alias='isVerified')
            blocked_until: str = Field(alias='blockedUntil')
            last_entry: str
            last_activity: str
            registration_date: str = Field(alias='registrationDate')
            language: str
            is_dnd: bool = Field(alias='isDnD')
            feedback_positive: int = Field(alias='feedbackPositive')
            feedback_negative: int = Field(alias='feedbackNegative')
            trades_completed_percent: float = Field(alias='tradesCompletedPercent')
            trades_completed: int = Field(alias='tradesCompleted')
            merchant: bool
            pro: bool

        offer: Offer
        user: User
        is_not_created: bool

    info: List[Info]


class GetViaOfferResponse(BaseModel):
    class Data(BaseModel):
        card: str
        id: str
        num_id: int
        token: str
        tech: str

    data: List[Data]


class PostOrdersInitRequest(BaseModel):
    internal_id: str
    taker: str
    maker: str
    amount_from: float
    amount_to: float
    crypto: str
    fiat: str
    req_id: str
    address: str


class PostOrdersInitResponse(BaseModel):
    data: str

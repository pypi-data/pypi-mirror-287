import requests

import p2p_exnode_sdk.models as models

BASE_URL = "https://api4.exnode.ru/api/proxy/"


def post_sign_in(request: models.PostSignInRequest) -> models.PostSignInResponse:
    url = f"{BASE_URL}5/user/sign_in"

    data = request.model_dump_json(by_alias=True)

    headers = {
        "Content-Type": "application/json",
        "User-agent": "Mozilla/5.0",
        "Ua": "Mozilla/5.0",
    }

    response = requests.post(url, data=data, headers=headers)
    response.raise_for_status()

    data = response.json()

    return models.PostSignInResponse(**data)


def get_active_offers(request: models.GetActiveOffersParams) -> models.GetActiveOffersResponse:
    url = f"{BASE_URL}4/market/offers/active"

    params = request.model_dump()

    headers = {
        "Content-Type": "application/json",
        "User-agent": "Mozilla/5.0",
        "Ua": "Mozilla/5.0",
    }

    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()

    data = response.json()

    return models.GetActiveOffersResponse(**data)


def get_via_offer(internal_id, access, refresh) -> models.GetViaOfferResponse:
    url = f"{BASE_URL}4/market/payments/via_offer/{internal_id}"

    headers = {
        "Access": access,
        "Refresh": refresh,
        "Content-Type": "application/json",
        "User-agent": "Mozilla/5.0",
        "Ua": "Mozilla/5.0",
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    data = response.json()

    return models.GetViaOfferResponse(**data)


def post_orders_init(request: models.PostOrdersInitRequest, access, refresh) -> models.PostOrdersInitResponse:
    url = f"{BASE_URL}4/market/orders/init"

    data = request.model_dump_json()

    headers = {
        "Access": access,
        "Refresh": refresh,
        "Content-Type": "application/json",
        "User-agent": "Mozilla/5.0",
        "Ua": "Mozilla/5.0",
    }

    response = requests.post(url, data=data, headers=headers)
    response.raise_for_status()

    data = response.json()

    return models.PostOrdersInitResponse(**data)

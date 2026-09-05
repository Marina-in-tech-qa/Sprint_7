import pytest
import requests

from helpers.courier_generator import (
    register_new_courier_and_return_login_password,
    delete_courier,
)
from helpers.order_helper import (
    create_order,
    get_order_id,
    cancel_order,
)
from urls import LOGIN_COURIER_URL


@pytest.fixture
def courier():
    login, password, first_name = (
        register_new_courier_and_return_login_password()
    )

    courier_data = {
        "login": login,
        "password": password,
        "firstName": first_name,
    }

    yield courier_data

    delete_courier(courier_data)


@pytest.fixture
def courier_with_id(courier):
    login_response = requests.post(
        LOGIN_COURIER_URL,
        data={
            "login": courier["login"],
            "password": courier["password"],
        },
    )

    courier_data = courier.copy()
    courier_data["id"] = login_response.json()["id"]

    return courier_data


@pytest.fixture
def courier_cleanup():
    couriers = []

    yield couriers

    for courier_data in couriers:
        delete_courier(courier_data)


@pytest.fixture
def order():
    track = create_order()
    order_id = get_order_id(track)

    order_data = {
        "track": track,
        "id": order_id,
    }

    yield order_data

    cancel_order(track)


@pytest.fixture
def order_cleanup():
    tracks = []

    yield tracks

    for track in tracks:
        cancel_order(track)
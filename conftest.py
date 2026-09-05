import pytest
import requests

from helpers.courier_generator import register_new_courier_and_return_login_password
from urls import LOGIN_COURIER_URL, DELETE_COURIER_URL


@pytest.fixture
def courier():
    login, password, first_name = register_new_courier_and_return_login_password()

    courier_data = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    yield courier_data

    login_response = requests.post(
        LOGIN_COURIER_URL,
        data={
            "login": login,
            "password": password
        }
    )

    if login_response.status_code == 200:
        courier_id = login_response.json()["id"]

        requests.delete(
            f"{DELETE_COURIER_URL}/{courier_id}"
        )
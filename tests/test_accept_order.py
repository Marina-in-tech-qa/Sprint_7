import allure
import requests

from helpers.order_helper import (
    create_order,
    get_order_id,
    cancel_order,
)
from urls import (
    LOGIN_COURIER_URL,
    ACCEPT_ORDER_URL,
)


@allure.feature("Принятие заказа курьером")
class TestAcceptOrder:

    @allure.title("Курьер может принять заказ")
    def test_accept_order_success(self, courier):
        track = create_order()

        try:
            with allure.step("Получить id курьера"):
                login_response = requests.post(
                    LOGIN_COURIER_URL,
                    data={
                        "login": courier["login"],
                        "password": courier["password"]
                    }
                )

                courier_id = login_response.json()["id"]

            with allure.step("Получить id созданного заказа"):
                order_id = get_order_id(track)

            with allure.step("Назначить заказ курьеру"):
                response = requests.put(
                    f"{ACCEPT_ORDER_URL}/{order_id}",
                    params={"courierId": courier_id}
                )

            with allure.step("Проверить успешное принятие заказа"):
                assert login_response.status_code == 200
                assert order_id is not None
                assert response.status_code == 200
                assert response.json() == {"ok": True}

        finally:
            cancel_order(track)
import allure
import requests

from urls import ACCEPT_ORDER_URL


@allure.feature("Принятие заказа курьером")
class TestAcceptOrder:

    @allure.title("Курьер может принять заказ")
    def test_accept_order_success(
        self,
        courier_with_id,
        order,
    ):
        courier_id = courier_with_id["id"]
        order_id = order["id"]

        with allure.step("Назначить заказ курьеру"):
            response = requests.put(
                f"{ACCEPT_ORDER_URL}/{order_id}",
                params={
                    "courierId": courier_id,
                },
            )

        with allure.step(
            "Проверить успешное принятие заказа"
        ):
            assert response.status_code == 200
            assert response.json() == {"ok": True}
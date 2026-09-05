import allure
import pytest
import requests

from data import ORDER_DATA
from urls import ORDERS_URL


@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title(
        "Можно создать заказ с вариантом цвета: {order_data[color]}"
    )
    @pytest.mark.parametrize(
        "order_data",
        [
            {
                **ORDER_DATA,
                "color": ["BLACK"],
            },
            {
                **ORDER_DATA,
                "color": ["GREY"],
            },
            {
                **ORDER_DATA,
                "color": ["BLACK", "GREY"],
            },
        ],
    )
    def test_create_order_with_color(
        self,
        order_data,
        order_cleanup,
    ):
        with allure.step("Отправить запрос на создание заказа"):
            response = requests.post(
                ORDERS_URL,
                json=order_data,
            )

        response_body = response.json()
        order_cleanup.append(response_body.get("track"))

        with allure.step(
            "Проверить успешное создание заказа"
        ):
            assert response.status_code == 201
            assert "track" in response_body
            assert isinstance(response_body["track"], int)

    @allure.title("Можно создать заказ без указания цвета")
    def test_create_order_without_color(self, order_cleanup):
        order_data = ORDER_DATA.copy()

        with allure.step(
            "Отправить запрос на создание заказа без цвета"
        ):
            response = requests.post(
                ORDERS_URL,
                json=order_data,
            )

        response_body = response.json()
        order_cleanup.append(response_body.get("track"))

        with allure.step(
            "Проверить успешное создание заказа"
        ):
            assert response.status_code == 201
            assert "track" in response_body
            assert isinstance(response_body["track"], int)
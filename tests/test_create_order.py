import allure
import pytest
import requests

from data import ORDER_DATA
from urls import ORDERS_URL


@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Можно создать заказ с разными вариантами цвета")
    @pytest.mark.parametrize(
        "color",
        [
            ["BLACK"],
            ["GREY"],
            ["BLACK", "GREY"],
            None,
        ]
    )
    def test_create_order_with_different_colors(self, color):
        order_data = ORDER_DATA.copy()

        with allure.step("Подготовить данные заказа"):
            if color is not None:
                order_data["color"] = color

        with allure.step("Отправить запрос на создание заказа"):
            response = requests.post(
                ORDERS_URL,
                json=order_data
            )

        response_body = response.json()

        with allure.step("Проверить успешное создание заказа"):
            assert response.status_code == 201
            assert "track" in response_body
            assert isinstance(response_body["track"], int)
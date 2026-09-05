import allure
import requests

from urls import ORDERS_URL


@allure.feature("Список заказов")
class TestOrdersList:

    @allure.title("В ответе возвращается список заказов")
    def test_orders_list_returns_orders(self):
        with allure.step("Запросить список заказов"):
            response = requests.get(ORDERS_URL)

        response_body = response.json()

        with allure.step("Проверить статус-код и наличие списка заказов"):
            assert response.status_code == 200
            assert "orders" in response_body
            assert isinstance(response_body["orders"], list)
import allure
import requests

from helpers.courier_generator import generate_courier_data
from urls import (
    CREATE_COURIER_URL,
    LOGIN_COURIER_URL,
    DELETE_COURIER_URL,
)


@allure.feature("Удаление курьера")
class TestDeleteCourier:

    @allure.title("Курьера можно удалить")
    def test_delete_courier_success(self):
        courier_data = generate_courier_data()

        with allure.step("Создать тестового курьера"):
            create_response = requests.post(
                CREATE_COURIER_URL,
                data=courier_data
            )

        with allure.step("Получить id созданного курьера"):
            login_response = requests.post(
                LOGIN_COURIER_URL,
                data={
                    "login": courier_data["login"],
                    "password": courier_data["password"]
                }
            )

            courier_id = login_response.json()["id"]

        with allure.step("Удалить курьера"):
            delete_response = requests.delete(
                f"{DELETE_COURIER_URL}/{courier_id}"
            )

        with allure.step("Проверить ответ сервера"):
            assert create_response.status_code == 201
            assert login_response.status_code == 200
            assert delete_response.status_code == 200
            assert delete_response.json() == {"ok": True}
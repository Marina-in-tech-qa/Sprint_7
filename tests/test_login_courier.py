import allure
import requests

from data import (
    LOGIN_NOT_ENOUGH_DATA_MESSAGE,
    LOGIN_USER_NOT_FOUND_MESSAGE,
)
from urls import LOGIN_COURIER_URL


@allure.feature("Логин курьера")
class TestLoginCourier:

    @allure.title("Курьер может авторизоваться")
    def test_login_courier_success(self, courier):
        with allure.step("Отправить корректные данные для авторизации"):
            response = requests.post(
                LOGIN_COURIER_URL,
                data={
                    "login": courier["login"],
                    "password": courier["password"]
                }
            )

        response_body = response.json()

        with allure.step("Проверить успешную авторизацию и наличие id"):
            assert response.status_code == 200
            assert "id" in response_body
            assert isinstance(response_body["id"], int)

    @allure.title("Нельзя авторизоваться с неверным паролем")
    def test_login_courier_with_wrong_password(self, courier):
        with allure.step("Отправить запрос с неверным паролем"):
            response = requests.post(
                LOGIN_COURIER_URL,
                data={
                    "login": courier["login"],
                    "password": "wrong_password"
                }
            )

        with allure.step("Проверить ошибку авторизации"):
            assert response.status_code == 404
            assert response.json() == LOGIN_USER_NOT_FOUND_MESSAGE

    @allure.title("Нельзя авторизоваться несуществующему курьеру")
    def test_login_nonexistent_courier(self):
        with allure.step("Отправить данные несуществующего курьера"):
            response = requests.post(
                LOGIN_COURIER_URL,
                data={
                    "login": "courier_that_does_not_exist_0905",
                    "password": "test12345"
                }
            )

        with allure.step("Проверить ответ для несуществующего пользователя"):
            assert response.status_code == 404
            assert response.json() == LOGIN_USER_NOT_FOUND_MESSAGE

    @allure.title("Нельзя авторизоваться без обязательного поля login")
    def test_login_courier_without_login(self):
        with allure.step("Отправить запрос без поля login"):
            response = requests.post(
                LOGIN_COURIER_URL,
                data={
                    "password": "test12345"
                }
            )

        with allure.step("Проверить ошибку недостаточности данных"):
            assert response.status_code == 400
            assert response.json() == LOGIN_NOT_ENOUGH_DATA_MESSAGE
import allure
import pytest
import requests

from data import (
    CREATE_COURIER_SUCCESS,
    COURIER_ALREADY_EXISTS_MESSAGE,
    COURIER_NOT_ENOUGH_DATA_MESSAGE,
)
from helpers.courier_generator import generate_courier_data
from urls import CREATE_COURIER_URL


@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Курьера можно создать")
    def test_create_courier_success(self, courier_cleanup):
        courier_data = generate_courier_data()
        courier_cleanup.append(courier_data)

        with allure.step("Отправить запрос на создание курьера"):
            response = requests.post(
                CREATE_COURIER_URL,
                data=courier_data,
            )

        with allure.step("Проверить статус-код и тело ответа"):
            assert response.status_code == 201
            assert response.json() == CREATE_COURIER_SUCCESS

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier(self, courier):
        with allure.step(
            "Повторно отправить данные зарегистрированного курьера"
        ):
            response = requests.post(
                CREATE_COURIER_URL,
                data=courier,
            )

        with allure.step(
            "Проверить ошибку повторного создания курьера"
        ):
            assert response.status_code == 409
            assert response.json() == COURIER_ALREADY_EXISTS_MESSAGE

    @allure.title(
        "Нельзя создать курьера без обязательного поля: {missing_field}"
    )
    @pytest.mark.parametrize(
        "missing_field",
        ["login", "password"],
    )
    def test_create_courier_without_required_field(
        self,
        missing_field,
    ):
        courier_data = generate_courier_data()
        courier_data.pop(missing_field)

        with allure.step(
            f"Отправить запрос без поля {missing_field}"
        ):
            response = requests.post(
                CREATE_COURIER_URL,
                data=courier_data,
            )

        with allure.step(
            "Проверить ошибку недостаточности данных"
        ):
            assert response.status_code == 400
            assert (
                response.json()
                == COURIER_NOT_ENOUGH_DATA_MESSAGE
            )
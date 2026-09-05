import allure
import requests

from urls import DELETE_COURIER_URL


@allure.feature("Удаление курьера")
class TestDeleteCourier:

    @allure.title("Курьера можно удалить")
    def test_delete_courier_success(self, courier_with_id):
        courier_id = courier_with_id["id"]

        with allure.step("Удалить зарегистрированного курьера"):
            response = requests.delete(
                f"{DELETE_COURIER_URL}/{courier_id}"
            )

        with allure.step(
            "Проверить успешное удаление курьера"
        ):
            assert response.status_code == 200
            assert response.json() == {"ok": True}
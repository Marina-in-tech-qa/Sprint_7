import allure

from helpers.order_helper import (
    create_order,
    get_order_by_track,
    cancel_order,
)


@allure.feature("Получение заказа по трек-номеру")
class TestGetOrder:

    @allure.title("Можно получить заказ по его track")
    def test_get_order_by_track_success(self):
        track = create_order()

        try:
            with allure.step("Получить созданный заказ по track"):
                response = get_order_by_track(track)

            response_body = response.json()

            with allure.step("Проверить статус и данные заказа"):
                assert response.status_code == 200
                assert "order" in response_body
                assert response_body["order"]["track"] == track

        finally:
            cancel_order(track)
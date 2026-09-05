import allure
import requests

from data import ORDER_DATA
from urls import (
    ORDERS_URL,
    CANCEL_ORDER_URL,
    GET_ORDER_BY_TRACK_URL,
)


@allure.step("Создать тестовый заказ")
def create_order():
    order_data = ORDER_DATA.copy()

    response = requests.post(
        ORDERS_URL,
        json=order_data
    )

    if response.status_code == 201:
        return response.json()["track"]

    return None


@allure.step("Получить заказ по трек-номеру {track}")
def get_order_by_track(track):
    return requests.get(
        GET_ORDER_BY_TRACK_URL,
        params={"t": track}
    )


@allure.step("Получить id заказа по трек-номеру {track}")
def get_order_id(track):
    response = get_order_by_track(track)

    if response.status_code == 200:
        return response.json()["order"]["id"]

    return None


@allure.step("Отменить тестовый заказ")
def cancel_order(track):
    if track is not None:
        requests.put(
            CANCEL_ORDER_URL,
            params={"track": track}
        )
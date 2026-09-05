CREATE_COURIER_SUCCESS = {"ok": True}

COURIER_ALREADY_EXISTS_MESSAGE = {
    "code": 409,
    "message": "Этот логин уже используется. Попробуйте другой."
}

COURIER_NOT_ENOUGH_DATA_MESSAGE = {
    "code": 400,
    "message": "Недостаточно данных для создания учетной записи"
}

LOGIN_NOT_ENOUGH_DATA_MESSAGE = {
    "code": 400,
    "message": "Недостаточно данных для входа"
}

LOGIN_USER_NOT_FOUND_MESSAGE = {
    "code": 404,
    "message": "Учетная запись не найдена"
}

ORDER_DATA = {
    "firstName": "Marina",
    "lastName": "Test",
    "address": "Test street 1",
    "metroStation": 4,
    "phone": "+79999999999",
    "rentTime": 2,
    "deliveryDate": "2026-09-10",
    "comment": "Sprint 7 test"
}
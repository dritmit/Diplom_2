import allure
import pytest
from helpers import Helpers
from data import Data
from stellarburgers_api import StellarBurgersApi


@allure.step("Фикстура регистрирует рандомного нового пользоателя в системе."
             "Возвращаем словарь с данными нового пользователя: email, логин, пароль и access токен."
             "Удаляет пользователя после выполнения проверки")
@pytest.fixture(scope='function')
def new_user():
    new_user_body = Data.user_create_random_body_valid
    new_user_body['email'] = Helpers.random_email(15)
    new_user_response = StellarBurgersApi.user_create(new_user_body)
    new_user_body["token"] = new_user_response.json()["accessToken"]
    new_user_body["status"] = new_user_response.status_code
    new_user_body["success"] = new_user_response.json()["success"]
    yield new_user_body
    headers = {"Authorization": new_user_body["token"]}
    StellarBurgersApi.user_delete(headers)

from stellarburgers_api import StellarBurgersApi
from data import Data
import allure
import pytest


class TestUserCreate:

    @allure.title('Проверка успешного создания пользователя')
    @allure.description('Вызываем ручку создания пользователя, передаем валидный набор данных пользователя:'
                        ' email, пароль и имя пользователя. Проверяем что ответ содаржит статус 200 и'
                        'в теле ответ ключ success в значении True')
    def test_user_create_success(self, new_user):

        assert new_user["status"] == 200 and new_user['success'] is True


    @allure.title('Проверка ошибки при создании пользователя, который уже зарегистрирован')
    @allure.description('Вызываем ручку создания пользователя, передаем валидный набор данных пользователя:'
                        ' email, пароль и имя пользователя. Вызываем ручку создания пользователя с тем же'
                        ' набором пользовательских данных повторно. Проверяем что ответ содаржит статус 403 и'
                        ' тело ответа соотствует описанию ручки')
    def test_user_create_double_fail(self, new_user):
        body = dict(email=new_user['email'], password=new_user['password'], name=new_user['name'])
        StellarBurgersApi.user_create(body)
        response = StellarBurgersApi.user_create(body)

        assert response.status_code == 403 and response.json() == Data.user_create_already_exists_response


    @allure.title('Проверка ошибки при создании пользователя с неполным набором регистрационных данных')
    @allure.description('Генеруем валидный набор данных пользователя: email, пароль и имя пользователя. '
                        'Удаляем один из ключей. Вызываем ручку создания пользователя с полученным неполным набором'
                        ' пользовательских данных. Проверяем что ответ содаржит статус 403 и'
                        ' тело ответа соотствует описанию ручки')
    @pytest.mark.parametrize("user_data", ["email", "password", "name"])
    def test_user_create_invalid_body(self, user_data):
        body = Data.user_create_random_body_valid
        body = {key: body[key] for key in body if key != user_data}
        response = StellarBurgersApi.user_create(body)

        assert response.status_code == 403 and response.json() == Data.user_create_body_invalid_response

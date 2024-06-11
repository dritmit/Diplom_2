import allure
from stellarburgers_api import StellarBurgersApi
import pytest
from data import Data


class TestUserProfileChange:

    @allure.title('Проверка успешного изменения данных пользователя с авторизацией')
    @allure.description('Создаем нового пользователя. Геренирируем новый набор пользовательских данных.'
                        'Вызываем ручку изменения данных пользователя, передаем токен и поочередно данные из нового'
                        ' набора: email, пароль и имя пользователя. Проверяем что ответ содержит статус 200 и '
                        'в ответе ключ success в значении True')
    @pytest.mark.parametrize("user_data", ["email", "password", "name"])
    def test_user_profile_change_with_authorization_success(self, new_user, user_data):
        another_user_body = Data.user_create_random_body_valid
        headers = {"Authorization": new_user['token']}
        body = {user_data: another_user_body[user_data]}
        user_change_response = StellarBurgersApi.user_profile_change(headers, body)

        assert user_change_response.status_code == 200 and user_change_response.json()['success'] is True

    @allure.title('Проверка ошибки при изменении данных пользователя без авторизации')
    @allure.description('Создаем нового пользователя. Геренирируем новый набор пользовательских данных.'
                        'Вызываем ручку изменения данных пользователя, передаем хедер без токена и поочередно'
                        ' данные из нового набора: email, пароль и имя пользователя.'
                        ' Проверяем что ответ содержит статус 401 и тело ответа соответствует документации'
                        ' и содаржит сообщение о необходимости авторизоваться')
    @pytest.mark.parametrize("user_data", ["email", "password", "name"])
    def test_user_profile_change_without_authorization_fail(self, new_user, user_data):
        another_user_body = Data.user_create_random_body_valid
        headers = {}
        body = {user_data: another_user_body[user_data]}
        user_change_response = StellarBurgersApi.user_profile_change(headers, body)

        assert user_change_response.status_code == 401 and\
               user_change_response.json() == Data.user_not_authorized_response

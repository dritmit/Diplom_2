from stellarburgers_api import StellarBurgersApi
from data import Data
import allure


class TestUserLogin:

    @allure.title('Проверка успешного создания заказа с валидным списком ингредиентов авторизованным пользователем ')
    @allure.description('Создаем нового пользователя. Вызываем ручку создания нового заказа, передаем access token '
                        'пользователя и валидный набор ингредиентов в теле запроса. Проверяем что статус ответа '
                        'равен 200 и в теле ответа ключ success в значении True.')
    def test_order_create_with_authorization_success(self, new_user):
        headers = {"Authorization": new_user['token']}
        order_create_response = StellarBurgersApi.order_create(headers, Data.order_create_body_valid)

        assert order_create_response.status_code == 200 and order_create_response.json()['success'] is True


    @allure.title('Проверка ошибки при создании заказа с пустым списком ингредиентов авторизованным пользователем')
    @allure.description('Создаем нового пользователя. Вызываем ручку создания нового заказа, передаем access token '
                        'пользователя и пустой список ингредиентов в теле запроса. Проверяем что статус ответа '
                        'равен 400 и в тело ответа соответствует описанию ручки и содержит уведомление об отсутствии '
                        'ингредиентов в запросе')
    def test_order_create_with_authorization_empty_ingredients_fail(self, new_user):
        headers = {"Authorization": new_user['token']}
        order_create_response = StellarBurgersApi.order_create(headers, Data.order_create_body_empty_ingredients)

        assert order_create_response.status_code == 400 and\
               order_create_response.json() == Data.order_create_empty_ingredients_response


    @allure.title('Проверка ошибки при создания заказа с невалидным списком ингредиентов авторизованным пользователем')
    @allure.description('Создаем нового пользователя. Вызываем ручку создания нового заказа, передаем access token '
                        'пользователя и невалидный список ингредиентов в теле запроса. Проверяем что статус ответа '
                        'равен 500')
    def test_order_create_with_authorization_invalid_ingredients_fail(self, new_user):
        headers = {"Authorization": new_user['token']}
        order_create_response = StellarBurgersApi.order_create(headers, Data.order_create_body_invalid)

        assert order_create_response.status_code == 500


    @allure.title('Проверка успешного создания заказа с валидным списком ингредиентов неавторизованным пользователем')
    @allure.description('Вызываем ручку создания нового заказа, передаем хедер без access token и валидный набор '
                        'ингредиентов в теле запроса. Проверяем что статус ответа '
                        'равен 200 и в теле ответа ключ success в значении True.')
    def test_order_create_without_authorization_success(self):
        headers = {}
        order_create_response = StellarBurgersApi.order_create(headers, Data.order_create_body_valid)

        assert order_create_response.status_code == 200 and order_create_response.json()['success'] is True


    @allure.title('Проверка ошибки при создании заказа с пустым списком ингредиентов неавторизованным пользователем')
    @allure.description('Вызываем ручку создания нового заказа, передаем хедер без access token и пустой набор '
                        'ингредиентов в теле запроса. Проверяем что статус ответа равен 200 и тело ответа'
                        ' соответствует описанию ручки и содержит уведомление об отсутствии ингредиентов в запросе')
    def test_order_create_without_authorization_empty_ingredients_fail(self):
        headers = {}
        order_create_response = StellarBurgersApi.order_create(headers, Data.order_create_body_empty_ingredients)

        assert order_create_response.status_code == 400 and \
               order_create_response.json() == Data.order_create_empty_ingredients_response


    @allure.title('Проверка ошибки при создании заказа с невалидным списком ингредиентов неавторизованным пользователем')
    @allure.description('Вызываем ручку создания нового заказа, передаем хедер без access token и невалидный список '
                        'ингредиентов в теле запроса. Проверяем что статус ответа равен 500')
    def test_order_create_without_authorization_invalid_ingredients_fail(self):
        headers = {}
        order_create_response = StellarBurgersApi.order_create(headers, Data.order_create_body_invalid)

        assert order_create_response.status_code == 500

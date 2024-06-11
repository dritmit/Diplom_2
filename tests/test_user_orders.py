from stellarburgers_api import StellarBurgersApi
from data import Data
import allure


class TestUserOrders:

    @allure.title('Проверка получения заказов авторизованного пользователя')
    @allure.description('Создаем нового пользователя, запоминаем access token, вызываем ручку создания заказа'
                        ' пользователя, передаем в хедере access token и валидное ингедиенты в теле запроса.'
                        '  Вызываем ручку получения списка заказов пользователя, передаем в хедере access token.'
                        ' Проверяем что ответ содаржит статус 200 и ключ success в значении True и в список заказов в '
                        'ключе orders не пустой')
    def test_user_orders_with_authorization_success(self, new_user):
        headers = {"Authorization": new_user['token']}
        StellarBurgersApi.order_create(headers, Data.order_create_body_valid)
        user_orders_response = StellarBurgersApi.user_orders(headers)

        assert user_orders_response.status_code == 200 and user_orders_response.json()["success"] and\
               len(user_orders_response.json()['orders']) > 0

    @allure.title('Проверка ошибки при получении заказов неавторизованного пользователя')
    @allure.description('Создаем нового пользователя, запоминаем access token, вызываем ручку создания заказа'
                        ' пользователя, передаем в хедере access token и валидное ингедиенты в теле запроса.'
                        ' Вызываем ручку получения списка заказов пользователя, передаем хедер без токена'
                        ' Проверяем что ответ содаржит статус 401 и тело ответа соответствует документации'
                        ' и содаржит сообщение о необходимости авторизоваться')
    def test_user_orders_without_authorization_fail(self, new_user):
        order_create_headers = {"Authorization": new_user['token']}
        user_orders_headers = {}
        StellarBurgersApi.order_create(order_create_headers, Data.order_create_body_valid)
        user_orders_response = StellarBurgersApi.user_orders(user_orders_headers)

        assert user_orders_response.status_code == 401 and \
               user_orders_response.json() == Data.user_not_authorized_response

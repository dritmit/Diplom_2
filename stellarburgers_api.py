import allure
import requests
import urls


class StellarBurgersApi:

    @staticmethod
    @allure.step("Регистрация пользователя")
    def user_create(body):
        return requests.post(f'{urls.BASE_URL}{urls.USER_CREATE_ENDPOINT}', json=body)


    @staticmethod
    @allure.step("Авторизация пользователя")
    def user_login(body):
        return requests.post(f'{urls.BASE_URL}{urls.USER_LOGIN_ENDPOINT}', json=body)


    @staticmethod
    @allure.step("Удаление пользователя")
    def user_delete(headers):
        return requests.delete(f'{urls.BASE_URL}{urls.USER_AUTHORIZATION_ENDPOINT}', headers=headers)


    @staticmethod
    @allure.step("Изменение данных пользователя")
    def user_profile_change(headers, body):
        return requests.patch(f'{urls.BASE_URL}{urls.USER_AUTHORIZATION_ENDPOINT}', headers=headers, json=body)


    @staticmethod
    @allure.step("Создание заказа")
    def order_create(headers, body):
        return requests.post(f'{urls.BASE_URL}{urls.ORDERS_ENDPOINT}', headers=headers, json=body)


    @staticmethod
    @allure.step("Получение заказов пользователя")
    def user_orders(headers):
        return requests.get(f'{urls.BASE_URL}{urls.ORDERS_ENDPOINT}', headers=headers)


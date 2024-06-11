from stellarburgers_api import StellarBurgersApi
import allure
from data import Data


class TestUserLogin:

    @allure.title('Проверка успешного входа в систему зарегистрированного пользователя')
    @allure.description('Создаем нового пользователя. Вызываем ручку авторизации, передаем в теле запроса'
                        ' email и пароль этого пользователя. Проверяем что статус ответа равен 200 и в теле '
                        'ответа ключ success в значении True')
    def test_user_login_success(self, new_user):
        body = dict(email=new_user['email'], password=new_user['password'])
        user_login_response = StellarBurgersApi.user_login(body)

        assert user_login_response.status_code == 200 and user_login_response.json()['success'] is True

    @allure.title('Проверка ошибки при входа в систему незарегистрированного пользователя')
    @allure.description('Вызываем ручку авторизации, передаем в теле запроса email и пароль '
                        'незарегистрированного пользователя. Проверяем что статус ответа равен 401 и тело ответа'
                        ' соответствует описанию ручки и содержит уведомление о том, что некорректны email или пароль')
    def test_user_login_not_exist_user_fail(self):
        user_login_response = StellarBurgersApi.user_login(Data.user_login_not_exist_data)

        assert user_login_response.status_code == 401 and \
               user_login_response.json() == Data.user_login_not_exist_response

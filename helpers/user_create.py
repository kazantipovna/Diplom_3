import allure
import requests
from faker import Faker

import urls


def create_test_user():
    """Создает словарь с данными тестового пользователя"""
    fake_data = Faker()
    test_user = {'email': fake_data.email(),
                 'password': fake_data.password(),
                 'name': fake_data.user_name()}
    return test_user


@allure.step('Регистрируем нового пользователя')
def register_new_user():
    """Регистрация тестового пользака через API"""
    user = create_test_user()
    payload = {"email": user['email'], "password": user['password'], "name": user['name']}
    response = requests.post(urls.reg_user_url, data=payload)
    user['accesstoken'] = response.json()['accessToken']
    return user


@allure.step('Удаляем пользователя')
def delete_user(user):
    """Удаление тестового пользака через API"""
    response = requests.delete(urls.del_user_url, headers={"authorization": user['accesstoken']})
    return response

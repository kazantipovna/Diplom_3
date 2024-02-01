from time import sleep

import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
import urls


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = urls.login_url
        self.locators = LoginPageLocators()

    @allure.step("Авторизоваться с логином")
    def login_fields_set(self, user):
        self.email_fieldset(user['email'])
        self.pass_fieldset(user['password'])
        self.login_btn_click()

    @allure.step('Заполняем поле email')
    def email_fieldset(self, email):
        self.get_element_put_text(self.locators.email_fieldset, email)

    @allure.step('Заполняем поле Пароль')
    def pass_fieldset(self, password):
        self.get_element_put_text(self.locators.pass_fieldset, password)

    @allure.step('Кликаем кнопку входа')
    def login_btn_click(self):
        self.get_web_element(self.locators.login_btn).click()

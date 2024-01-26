from selenium.webdriver.common.by import By

from pages.base_page import BasePage
import urls


class LoginPageLocators:
    """Класс локаторов"""
    recover_pass = By.XPATH, './/a[text()="Восстановить пароль"]'
    login_btn = By.XPATH, './/button[text()="Войти"]'
    email_fieldset = By.XPATH, './/fieldset[1]//input'
    pass_fieldset = By.XPATH, './/fieldset[2]//input'
    header_h2 = By.XPATH, './/h2'


class LoginPage(BasePage):
    """Класс страницы логина"""

    def __init__(self, driver):
        super().__init__(driver)
        self.url = urls.login_url
        self.locators = LoginPageLocators()

    @property
    def recover_pass(self):
        return self.get_web_element(self.locators.recover_pass)

    @property
    def login_btn(self):
        return self.get_web_element(self.locators.login_btn)

    @property
    def email_fieldset(self):
        return self.get_web_element(self.locators.email_fieldset)

    @property
    def pass_fieldset(self):
        return self.get_web_element(self.locators.pass_fieldset)

    @property
    def header_h2(self):
        return self.get_web_element(self.locators.header_h2)

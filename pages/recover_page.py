import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
import urls


class RecoverPageLocators:
    """Класс локаторов"""
    recover_pass_btn = By.XPATH, './/button[text()="Восстановить"]'
    header_h2 = By.XPATH, './/h2'  # любой заголовок h2
    email_field = By.XPATH, '//input[@name="name"]'
    email_fieldset = By.XPATH, './/fieldset[1]//input'
    recover_pass_header = By.XPATH, './/h2[text()="Восстановление пароля"]'
    save_btn = By.XPATH, './/button[text()="Сохранить"]'
    password_field = By.XPATH, '//input[@label="Пароль"]'
    eye_btn = By.CLASS_NAME, 'input__icon' #input__icon input__icon-action
    recover_pass_set = By.XPATH, './/fieldset[1]//label'


class RecoverPage(BasePage):
    """Класс страницы восстановления пароля"""

    def __init__(self, driver):
        super().__init__(driver)
        self.url = urls.recover_url
        self.locators = RecoverPageLocators()

    @property
    def recover_pass_btn(self):
        return self.get_web_element(self.locators.recover_pass_btn)

    @property
    def header_h2(self):
        return self.get_web_element(self.locators.header_h2)

    @property
    def email_field(self):
        return self.get_web_element(self.locators.email_field)

    @property
    def email_fieldset(self):
        return self.get_web_element(self.locators.email_fieldset)

    @property
    def recover_pass_header(self):
        return self.get_web_element(self.locators.recover_pass_header)

    @property
    def save_btn(self):
        return self.get_web_element(self.locators.save_btn)

    @property
    def eye_btn(self):
        return self.get_web_element(self.locators.eye_btn)

    @property
    def password_field(self):
        return self.get_web_element(self.locators.password_field)

    @property
    def recover_pass_set(self):
        return self.get_web_element(self.locators.recover_pass_set)

    @allure.step('Заполняем поле имейлом')
    def recover_set_email(self, user):
        """Заполняет поле имейлом"""
        self.driver.get(self.url)
        self.email_field.click()
        self.email_fieldset.send_keys(user['email'])

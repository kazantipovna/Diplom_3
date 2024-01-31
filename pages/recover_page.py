import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
import urls


class RecoverPageLocators:
    recover_pass_btn = By.XPATH, './/button[text()="Восстановить"]'
    header_h2 = By.XPATH, './/h2'  # любой заголовок h2
    email_field = By.XPATH, '//input[@name="name"]'
    save_btn = By.XPATH, './/button[text()="Сохранить"]'
    eye_btn = By.CLASS_NAME, 'input__icon'
    recover_pass_set = By.XPATH, './/label[text()="Пароль"]'


class RecoverPage(BasePage):

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
    def save_btn(self):
        return self.get_web_element(self.locators.save_btn)

    @property
    def eye_btn(self):
        return self.get_web_element(self.locators.eye_btn)

    @property
    def recover_pass_set(self):
        return self.get_web_element(self.locators.recover_pass_set)

    @allure.step('Заполняем поле имейлом')
    def recover_set_email(self, user):
        self.driver.get(self.url)
        self.email_field.click()
        self.email_field.send_keys(user['email'])

    @allure.step('Получаем название класса для проверки активности поля')
    def check_active_email_input_1(self):
        return self.wait_for_element_is_visible(RecoverPageLocators.recover_pass_set).get_attribute("class")

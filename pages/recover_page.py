import allure

from locators.recover_page_locators import RecoverPageLocators
from pages.base_page import BasePage
import urls


class RecoverPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = urls.recover_url
        self.locators = RecoverPageLocators()

    @allure.step('Заполняем поле имейлом')
    def email_field_set(self, email):
        self.get_element_put_text(self.locators.email_field, email)

    @allure.step('Заполняем поле имейлом')
    def recover_set_email(self, user):
        self.email_field_set(user['email'])

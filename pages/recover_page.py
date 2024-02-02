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

    @allure.step('Получаем значение введенного имейла')
    def recover_get_email(self):
        email_value = self.get_web_element(self.locators.email_field).get_attribute('value')
        return email_value

    @allure.step('Кликаем кнопку восстановления пароля')
    def recover_recover_click(self):
        self.click_element(self.locators.recover_pass_btn)

    @allure.step('Кликаем "глаз" в поле пароля')
    def recover_eye_click(self):
        self.click_element(self.locators.eye_btn)

    @allure.step('Проверяем, что страничка ЛК загрузилась')
    def check_recover_page(self):
        element_text = self.get_element_text(self.locators.header_recover)
        assert 'Восстановление пароля' in element_text, \
            f'Ошибка: не осуществлен переход на страницу восстановления пароля по кнопке «Восстановить пароль»'

    @allure.step('Проверяем, что страничка ЛК загрузилась')
    def check_eye_class_name(self):
        assert 'input__placeholder-focused' in self.get_class_name(RecoverPageLocators.recover_pass_set), \
            f'Ошибка: не подсветилось поле "Пароль" после нажатия на глаз'

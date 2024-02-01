import allure

import helpers.user_actions as actions
from locators.login_page_locators import LoginPageLocators
from locators.recover_page_locators import RecoverPageLocators


@allure.feature('Восстановление пароля')
class TestRecovers:
    @allure.title('Кнопка «Восстановить пароль»')
    @allure.description('переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_recover(self, driver):
        login_page = actions.get_login_page(driver)
        login_page.click_element(LoginPageLocators.recover_pass)
        element_text = login_page.get_element_text(LoginPageLocators.header_recover)
        assert 'Восстановление пароля' in element_text, \
            f'Ошибка: не осуществлен переход на страницу восстановления пароля по кнопке «Восстановить пароль»'

    @allure.title('Ввод почты для восстановления')
    @allure.description('Ввод почты для восстановления пароля')
    def test_recover_fill_email_field(self, driver, user):
        recovery_page = actions.recovery_page_set_email(driver, user)
        result = recovery_page.get_web_element(RecoverPageLocators.email_field).get_attribute('value')
        expected_result = user['email']
        assert result == expected_result, \
            f'Ошибка: введенный адрес не соответствует ожидаемому, {result} вместо {expected_result}'

    @allure.title('Кнопка «Восстановить»')
    @allure.description('ввод почты и клик по кнопке «Восстановить»')
    def test_recover_btn_click(self, driver, user):
        recovery_page = actions.recovery_page_set_email(driver, user)
        recovery_page.click_element(RecoverPageLocators.recover_pass_btn)
        element_text = recovery_page.get_element_text(LoginPageLocators.header_recover)
        assert 'Восстановление пароля' in element_text, f'Ошибка: не нажалась кнопка «Восстановить»'

    @allure.title('Кнопка "показать/скрыть пароль"')
    @allure.description('клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_recover_pass_field_active(self, driver, user):
        recovery_page = actions.recovery_page_set_email(driver, user)
        recovery_page.click_element(RecoverPageLocators.recover_pass_btn)
        recovery_page.click_element(RecoverPageLocators.eye_btn)
        assert 'input__placeholder-focused' in recovery_page.get_class_name(RecoverPageLocators.recover_pass_set), \
            f'Ошибка: не подсветилось поле "Пароль" после нажатия на глаз'

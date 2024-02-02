import allure

from pages.login_page import LoginPage
from pages.recover_page import RecoverPage


@allure.feature('Восстановление пароля')
class TestRecovers:
    @allure.title('Кнопка «Восстановить пароль»')
    @allure.description('переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_recover(self, driver):
        login_page = LoginPage(driver)
        login_page.open(login_page.url)
        login_page.login_recover_click()
        recovery_page = RecoverPage(driver)
        recovery_page.check_recover_page()

    @allure.title('Ввод почты для восстановления')
    @allure.description('Ввод почты для восстановления пароля')
    def test_recover_fill_email_field(self, driver, user):
        recovery_page = RecoverPage(driver)
        recovery_page.open(recovery_page.url)
        recovery_page.recover_set_email(user)
        result = recovery_page.recover_get_email()
        expected_result = user['email']
        assert result == expected_result, \
            f'Ошибка: введенный адрес не соответствует ожидаемому, {result} вместо {expected_result}'

    @allure.title('Кнопка «Восстановить»')
    @allure.description('ввод почты и клик по кнопке «Восстановить»')
    def test_recover_btn_click(self, driver, user):
        recovery_page = RecoverPage(driver)
        recovery_page.open(recovery_page.url)
        recovery_page.recover_set_email(user)
        recovery_page.recover_recover_click()
        recovery_page.check_recover_page()

    @allure.title('Кнопка "показать/скрыть пароль"')
    @allure.description('клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_recover_pass_field_active(self, driver, user):
        recovery_page = RecoverPage(driver)
        recovery_page.open(recovery_page.url)
        recovery_page.recover_set_email(user)
        recovery_page.recover_recover_click()
        recovery_page.recover_eye_click()
        recovery_page.check_eye_class_name()

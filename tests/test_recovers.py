import allure

from pages.login_page import LoginPage
from pages.recover_page import RecoverPage, RecoverPageLocators
import urls


@allure.feature('Восстановление пароля')
class TestRecovers:
    @allure.title('Кнопка «Восстановить пароль»')
    @allure.description('переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_recover(self, driver):
        login_page = LoginPage(driver)
        login_page.open(urls.login_url)
        login_page.click_web_element(login_page.recover_pass)
        assert login_page.header_h2.text == 'Восстановление пароля', \
            f'Ошибка: не осуществлен переход на страницу восстановления пароля по кнопке «Восстановить пароль»'

    @allure.title('Ввод почты для восстановления')
    @allure.description('Ввод почты для восстановления пароля')
    def test_recover_fill_email_field(self, driver, user):
        recover_page = RecoverPage(driver)
        recover_page.recover_set_email(user)
        result = recover_page.email_field.get_attribute('value')
        expected_result = user['email']
        assert result == expected_result, \
            f'Ошибка: введенный адрес не соответствует ожидаемому, {result} вместо {expected_result}'

    @allure.title('Кнопка «Восстановить»')
    @allure.description('ввод почты и клик по кнопке «Восстановить»')
    def test_recover_btn_click(self, driver, user):
        recover_page = RecoverPage(driver)
        recover_page.recover_set_email(user)
        recover_page.click_web_element(recover_page.recover_pass_btn)
        assert recover_page.save_btn.is_displayed(), f'Ошибка: не нажалась кнопка «Восстановить»'

    @allure.title('Кнопка "показать/скрыть пароль"')
    @allure.description('клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_recover_pass_field_active(self, driver, user):
        recover_page = RecoverPage(driver)
        recover_page.recover_set_email(user)
        recover_page.click_web_element(recover_page.recover_pass_btn)
        recover_page.click_web_element(recover_page.eye_btn)
        assert ('input__placeholder-focused' in
                driver.find_element(*RecoverPageLocators.recover_pass_set).get_attribute("class")), \
            f'Ошибка: не подсветилось поле "Пароль" после нажатия на глз'

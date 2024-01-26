import allure

import helpers.user_actions as actions
from pages.login_page import LoginPage
import urls


@allure.feature('Раздел «Личный кабинет»')
class TestLK:

    @allure.title('Переход в «Личный кабинет»')
    @allure.description('переход по клику на «Личный кабинет» с основной страницы')
    def test_go_to_lk(self, driver, user):
        assert actions.login_and_go_to_lk(driver, user), f'Ошибка: не осуществлен переход в ЛК'

    @allure.title('Переход в «История заказов»')
    @allure.description('переход в раздел «История заказов» в личном кабинете')
    def test_go_to_orders_history(self, driver, user):
        lk = actions.login_and_go_to_lk(driver, user)
        lk.click_web_element(lk.lk_history)
        assert driver.current_url == urls.lk_history_url, f'Ошибка: не осуществлен переход в п/м «История заказов»'

    @allure.title('Выход из аккаунта')
    @allure.description('выход из аккаунта')
    def test_logout(self, driver, user):
        lk = actions.login_and_go_to_lk(driver, user)
        lk.click_web_element(lk.lk_exit)
        login = LoginPage(driver)
        assert login.login_btn.is_displayed(), f'Ошибка: не осуществлен выход из системы'

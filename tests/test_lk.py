import allure

from pages.history_page import HistoryPage
from pages.lk_page import LkPage
from pages.login_page import LoginPage


@allure.feature('Раздел «Личный кабинет»')
class TestLK:

    @allure.title('Переход в «Личный кабинет»')
    @allure.description('переход по клику на «Личный кабинет» с основной страницы')
    def test_go_to_lk(self, driver, user, login):
        lk_page = LkPage(driver)
        lk_page.lk_btn_click()
        lk_page.check_profile_page()

    @allure.title('Переход в «История заказов»')
    @allure.description('переход в раздел «История заказов» в личном кабинете')
    def test_go_to_orders_history(self, driver, user, login):
        lk_page = LkPage(driver)
        lk_page.lk_btn_click()
        lk_page.lk_history_click()
        history_page = HistoryPage(driver)
        history_page.check_history_url()

    @allure.title('Выход из аккаунта')
    @allure.description('выход из аккаунта')
    def test_logout(self, driver, user, login):
        lk_page = LkPage(driver)
        lk_page.lk_btn_click()
        lk_page.lk_exit_click()
        login_page = LoginPage(driver)
        login_page.check_login_page()

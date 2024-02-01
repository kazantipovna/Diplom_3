import allure

import helpers.user_actions as actions
from pages.history_page import HistoryPage
from locators.lk_page_locators import LkPageLocators
from locators.login_page_locators import LoginPageLocators
import urls


@allure.feature('Раздел «Личный кабинет»')
class TestLK:

    @allure.title('Переход в «Личный кабинет»')
    @allure.description('переход по клику на «Личный кабинет» с основной страницы')
    def test_go_to_lk(self, driver, user):
        lk = actions.login_and_go_to_lk(driver, user)
        element_text = lk.get_element_text(LkPageLocators.lk_profile)
        assert 'Профиль' in element_text, f'Ошибка: не осуществлен переход в ЛК'

    @allure.title('Переход в «История заказов»')
    @allure.description('переход в раздел «История заказов» в личном кабинете')
    def test_go_to_orders_history(self, driver, user):
        lk = actions.login_and_go_to_lk(driver, user)
        lk.click_element(LkPageLocators.lk_history)
        history = HistoryPage(driver)
        curr_url = history.get_curr_url()
        assert curr_url == urls.lk_history_url, f'Ошибка: не осуществлен переход в п/м «История заказов»'

    @allure.title('Выход из аккаунта')
    @allure.description('выход из аккаунта')
    def test_logout(self, driver, user):
        lk = actions.login_and_go_to_lk(driver, user)
        lk.lk_exit_click()
        element_text = lk.get_element_text(LoginPageLocators.header_enter)
        assert 'Вход' in element_text, f'Ошибка: не осуществлен выход из системы'

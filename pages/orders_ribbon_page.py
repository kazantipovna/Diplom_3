import allure

from locators.orders_ribbon_page_locators import RibbonPageLocators
from pages.base_page import BasePage
import urls


class RibbonPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = urls.ribbon_url
        self.locators = RibbonPageLocators()

    @allure.step('Кликаем верхний заказ')
    def click_last_order(self):
        self.click_element(self.locators.last_order)

    @allure.step('Получаем количество всех заказов')
    def get_all_orders_count(self):
        # self.open(urls.ribbon_url)
        all_orders = int(self.get_element_text(self.locators.all_orders))
        return all_orders

    @allure.step('Получаем количество сегодняшних заказов')
    def get_today_orders_count(self):
        self.open(urls.ribbon_url)
        today_orders = int(self.get_element_text(self.locators.today_orders))
        return today_orders

    @allure.step('Получаем заказы в работе')
    def get_orders_in_work(self):
        self.open(urls.ribbon_url)
        orders_in_work = str(self.get_element_text(self.locators.orders_in_work))
        return orders_in_work

    @allure.step('Получаем готовые заказы')
    def get_orders_done(self):
        self.open(urls.ribbon_url)
        orders_done = str(self.get_element_text(self.locators.orders_done))
        return orders_done

    @allure.step('Проверяем, что страничка ЛК загрузилась')
    def check_orders_ribbon_page(self):
        element_text = self.get_element_text(self.locators.orders_ribbon_header)
        assert 'Лента заказов' in element_text, f'Ошибка: не осуществлен переход в «Лента заказов»'

    @allure.step('Проверяем, что панель с составом заказа отобразилась')
    def check_order_compound(self):
        element_text = self.get_element_text(self.locators.order_compound)
        assert 'Cостав' in element_text, f'Ошибка: не отобразилась панель ингредиента'

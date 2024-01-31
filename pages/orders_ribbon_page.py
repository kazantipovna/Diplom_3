import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
import urls


class RibbonPageLocators:
    orders_ribbon_header = By.XPATH, './/h1[text()="Лента заказов"]'
    last_order = By.XPATH, './/div[contains(@class,"OrderHistory_dataBox__1mkxK")]'
    order_panel = By.XPATH, './/div[contains(@class,"Modal_orderBox__1xWdi")]'
    all_orders = By.XPATH, './/div[2]/p[contains(@class,"OrderFeed_number__2MbrQ")]'
    today_orders = By.XPATH, './/div[3]/p[contains(@class,"OrderFeed_number__2MbrQ")]'
    orders_in_work = By.XPATH, './/ul[2]/li[contains(@class,"text text_type_digits-default")]'
    orders_done = By.XPATH, './/div[1]/ul[1][contains(@class,"OrderFeed_orderList")]'


class RibbonPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = urls.ribbon_url
        self.locators = RibbonPageLocators()

    @property
    def orders_ribbon_header(self):
        return self.get_web_element(self.locators.orders_ribbon_header)

    @property
    def last_order(self):
        return self.get_web_element(self.locators.last_order)

    @property
    def order_panel(self):
        return self.get_web_element(self.locators.order_panel)

    @property
    def all_orders(self):
        return self.get_web_element(self.locators.all_orders)

    @property
    def today_orders(self):
        return self.get_web_element(self.locators.today_orders)

    @property
    def orders_in_work(self):
        return self.get_web_element(self.locators.orders_in_work)

    @property
    def orders_done(self):
        return self.get_web_element(self.locators.orders_done)

    @allure.step('Получаем количество всех заказов')
    def get_all_orders_count(self):
        self.open(urls.ribbon_url)
        all_orders = self.all_orders.text
        return all_orders

    @allure.step('Получаем количество сегодняшних заказов')
    def get_today_orders_count(self):
        self.open(urls.ribbon_url)
        today_orders = self.today_orders.text
        return today_orders

    @allure.step('Получаем заказы в работе')
    def get_orders_in_work(self):
        self.open(urls.ribbon_url)
        orders_in_work = self.orders_in_work.text
        return orders_in_work

    @allure.step('Получаем готовые заказы')
    def get_orders_done(self):
        self.open(urls.ribbon_url)
        orders_done = self.orders_done.text
        return orders_done


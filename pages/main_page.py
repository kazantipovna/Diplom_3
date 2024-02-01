import allure
from selenium.webdriver import ActionChains

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import urls


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = urls.main_url
        self.locators = MainPageLocators()

    @allure.step('Добавляем ингредиент в бургер')
    def add_ingredient(self, driver):
        action_chains = ActionChains(driver)
        element = self.get_web_element(self.locators.ingredient)
        target = self.get_web_element(self.locators.burger_constructor_basket)
        action_chains.drag_and_drop(element, target).perform()

    @allure.step('Добавляем необходимое количество ингредиентов')
    def add_some_ingredients(self, driver, count_ingr):
        for ingr in range(count_ingr):
            self.add_ingredient(driver)

    @allure.step('Добавляем булку в бургер')
    def add_bun(self, driver):
        action_chains = ActionChains(driver)
        element = self.get_web_element(self.locators.bun)
        target = self.get_web_element(self.locators.burger_constructor_basket)
        action_chains.drag_and_drop(element, target).perform()

    @allure.step('Получаем номер заказа')
    def get_order_number(self):
        order_number = str(self.get_element_text(self.locators.order_number))
        return order_number

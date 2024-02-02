import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import urls


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = urls.main_url
        self.locators = MainPageLocators()

    @allure.step('Кликаем конструктор')
    def click_constructor(self):
        self.click_element(self.locators.constructor)

    @allure.step('Кликаем ленту заказов')
    def click_orders_ribbon(self):
        self.click_element(self.locators.orders_ribbon)

    @allure.step('Кликаем ингредиент')
    def click_ingredient(self):
        self.click_element(self.locators.ingredient)

    @allure.step('Закрываем форму ингредиента по кресту')
    def click_cross_btn(self):
        self.click_element(self.locators.cross_btn)

    @allure.step('Кликаем "Оформить заказ"')
    def click_order_btn(self):
        self.click_element(self.locators.order_btn)

    @allure.step('Ожидаем пока 9999 изменится на номер заказа')
    def wait_def_num_invisibility(self):
        self.wait_for_element_invisibility(self.locators.default_order_number)

    @allure.step('Добавляем ингредиент в бургер')
    def add_ingredient(self, driver):
        element_locator = self.locators.ingredient
        target_locator = self.locators.burger_constructor_basket
        self.run_action_chains(driver, element_locator, target_locator)

    @allure.step('Добавляем необходимое количество ингредиентов')
    def add_some_ingredients(self, driver, count_ingr):
        for ingr in range(count_ingr):
            self.add_ingredient(driver)

    @allure.step('Добавляем булку в бургер')
    def add_bun(self, driver):
        element_locator = self.locators.bun
        target_locator = self.locators.burger_constructor_basket
        self.run_action_chains(driver, element_locator, target_locator)

    @allure.step('Создаем бургер и жмем "Оформить заказ"')
    def create_burger(self, driver):
        self.click_constructor()
        self.add_bun(driver)
        self.add_ingredient(driver)
        self.click_order_btn()
        self.wait_def_num_invisibility()
        order_number = self.get_order_number()
        self.click_cross_btn()
        return order_number

    @allure.step('Получаем номер заказа')
    def get_order_number(self):
        order_number = str(self.get_element_text(self.locators.order_number))
        return order_number

    @allure.step('Получаем количество добавленных ингредиентов')
    def get_ingr_count(self):
        ingr_count = self.get_element_text(self.locators.ingr_count)
        return ingr_count

    @allure.step('Проверяем, что страничка ЛК загрузилась')
    def check_main_page(self):
        element_text = self.get_element_text(self.locators.create_burger_header)
        assert 'Соберите бургер' in element_text, f'Ошибка: не осуществлен переход в «Конструктор»'

    @allure.step('Проверяем, что открылась формочка с деталями ингредиента')
    def check_ingr_details_form(self):
        element_text = self.get_element_text(self.locators.ingr_text)
        assert 'Детали ингредиента' in element_text, f'Ошибка: нет формы "Детали ингредиента"'

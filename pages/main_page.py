import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
import urls


class MainPageLocators:
    order_btn = By.XPATH, './/button[text()="Оформить заказ"]'
    lk_btn = By.XPATH, './/p[text()="Личный Кабинет"]'
    constructor = By.XPATH, './/p[text()="Конструктор"]'
    orders_ribbon = By.XPATH, './/p[text()="Лента Заказов"]'
    create_burger_header = By.XPATH, './/h1[text()="Соберите бургер"]'
    ingredient = By.XPATH, './/ul[3]/a[1]/img[contains(@class,"BurgerIngredient_ingredient")]'
    ingr_count = By.XPATH, './/ul[3]/a[1]/div[1]/p[contains(@class,"counter_counter")]'
    bun = By.XPATH, './/ul[1]/a[1]/img[contains(@class,"BurgerIngredient_ingredient")]'
    ingredient_details = By.XPATH, './/h2[text()="Детали ингредиента"]'
    cross_btn = By.XPATH, './/button[@type="button"]'
    burger_constructor_basket = By.XPATH, './/ul[contains(@class,"BurgerConstructor_basket")]'
    order_msg_panel = By.XPATH, '//div[contains(@class,"Modal_modal__contentBox__sCy8X")]'
    order_number = By.XPATH, '//div/h2[contains(@class,"Modal_modal__title_shadow")]'
    default_order_number = By.XPATH, '//div/h2[text()="9999"]'


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = urls.main_url
        self.locators = MainPageLocators()

    @property
    def order_btn(self):
        return self.get_web_element(self.locators.order_btn)

    @property
    def lk_btn(self):
        return self.get_web_element(self.locators.lk_btn)

    @property
    def constructor(self):
        return self.get_web_element(self.locators.constructor)

    @property
    def orders_ribbon(self):
        return self.get_web_element(self.locators.orders_ribbon)

    @property
    def create_burger_header(self):
        return self.get_web_element(self.locators.create_burger_header)

    @property
    def ingredient(self):
        return self.get_web_element(self.locators.ingredient)

    @property
    def bun(self):
        return self.get_web_element(self.locators.bun)

    @property
    def ingredient_details(self):
        return self.get_web_element(self.locators.ingredient_details)

    @property
    def cross_btn(self):
        return self.get_web_element(self.locators.cross_btn)

    @property
    def burger_constructor_basket(self):
        return self.get_web_element(self.locators.burger_constructor_basket)

    @property
    def ingr_count(self):
        return self.get_web_element(self.locators.ingr_count)

    @property
    def order_msg_panel(self):
        return self.get_web_element(self.locators.order_msg_panel)

    @property
    def order_number(self):
        return self.get_web_element(self.locators.order_number)

    @allure.step('Добавляем ингредиент в бургер')
    def add_ingredient(self, driver):
        """Добавляет ингредиент в бургер"""
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
    def get_order_number_text(self):
        text = self.order_number.text
        return text

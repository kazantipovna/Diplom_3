import allure

import helpers.user_actions as actions
from pages.main_page import MainPage
from pages.orders_ribbon_page import RibbonPage
from locators.main_page_locators import MainPageLocators
from locators.orders_ribbon_page_locators import RibbonPageLocators


@allure.feature('Проверка основного функционала')
class TestMainFunctional:

    @allure.title('Переход в «Конструктор»')
    @allure.description('переход по клику на «Конструктор»')
    def test_go_to_constructor(self, driver):
        actions.get_ribbon_page(driver)
        main_page = MainPage(driver)
        main_page.click_element(MainPageLocators.constructor)
        element_text = main_page.get_element_text(MainPageLocators.create_burger_header)
        assert 'Соберите бургер' in element_text, f'Ошибка: не осуществлен переход в «Конструктор»'

    @allure.title('Переход в «Лента заказов»')
    @allure.description('переход по клику на «Лента заказов»')
    def test_go_to_orders_ribbon(self, driver):
        main_page = actions.get_main_page(driver)
        main_page.click_element(MainPageLocators.orders_ribbon)
        ribbon_page = RibbonPage(driver)
        element_text = ribbon_page.get_element_text(RibbonPageLocators.orders_ribbon_header)
        assert 'Лента заказов' in element_text, f'Ошибка: не осуществлен переход в «Лента заказов»'

    @allure.title('Детали ингредиента')
    @allure.description('если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_get_ingredient_details(self, driver):
        ingr_form = actions.get_ingredient_form(driver)
        element_text = ingr_form.get_element_text(MainPageLocators.ingr_text)
        assert 'Детали ингредиента' in element_text, f'Ошибка: нет формы "Детали ингредиента"'

    @allure.title('Детали ингредиента закрываются по крестику')
    @allure.description('всплывающее окно формы "Детали ингредиента" закрывается кликом по крестику')
    def test_close_ingredient_details(self, driver):
        ingr_form = actions.get_ingredient_form(driver)
        ingr_form.click_element(MainPageLocators.cross_btn)
        element_text = ingr_form.get_element_text(MainPageLocators.create_burger_header)
        assert 'Соберите бургер' in element_text, f'Ошибка: "Детали ингредиента" не закрылись по крестику'

    @allure.title('Счетчик ингредиента')
    @allure.description('при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_ingredients_count(self, driver, count_ingr=2):
        main_page = actions.get_main_page(driver)
        main_page.add_some_ingredients(driver, count_ingr)
        result = main_page.get_element_text(MainPageLocators.ingr_count)
        assert result == str(count_ingr), f'Ошибка: не отработал счетчик ингредиента, {result} вместо {count_ingr}'

    @allure.title('Успешное оформление заказа')
    @allure.description('залогиненный пользователь может оформить заказ')
    def test_create_order_success(self, driver, user):
        main_page = actions.login_and_set_burger(driver, user)
        element_text = main_page.get_element_text(MainPageLocators.order_msg_panel)
        assert 'идентификатор заказа' in element_text, f'Ошибка: нет формы с деталями заказа после оформления'

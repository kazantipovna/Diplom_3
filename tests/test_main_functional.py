import allure

import helpers.user_actions as actions
from pages.main_page import MainPage
from pages.orders_ribbon_page import RibbonPage


@allure.feature('Проверка основного функционала')
class TestMainFunctional:

    @allure.title('Переход в «Конструктор»')
    @allure.description('переход по клику на «Конструктор»')
    def test_go_to_constructor(self, driver):
        ribbon_page = RibbonPage(driver)
        main_page = MainPage(driver)
        ribbon_page.open(ribbon_page.url)
        main_page.click_web_element(main_page.constructor)
        assert main_page.create_burger_header.is_displayed(), f'Ошибка: не осуществлен переход в «Конструктор»'

    @allure.title('Переход в «Лента заказов»')
    @allure.description('переход по клику на «Лента заказов»')
    def test_go_to_orders_ribbon(self, driver):
        main_page = actions.get_main_page(driver)
        main_page.click_web_element(main_page.orders_ribbon)
        ribbon_page = RibbonPage(driver)
        assert ribbon_page.orders_ribbon_header.is_displayed(), f'Ошибка: не осуществлен переход в «Лента заказов»'

    @allure.title('Детали ингредиента')
    @allure.description('если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_get_ingredient_details(self, driver):
        ingr_form = actions.get_ingredient_form(driver)
        assert ingr_form.ingredient_details.is_displayed(), f'Ошибка: нет формы "Детали ингредиента"'

    @allure.title('Детали ингредиента закрываются по крестику')
    @allure.description('всплывающее окно формы "Детали ингредиента" закрывается кликом по крестику')
    def test_close_ingredient_details(self, driver):
        ingr_form = actions.get_ingredient_form(driver)
        ingr_form.click_web_element(ingr_form.cross_btn)
        assert ingr_form.create_burger_header.text == 'Соберите бургер', \
            f'Ошибка: "Детали ингредиента" не закрылись по крестику'

    @allure.title('Счетчик ингредиента')
    @allure.description('при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_ingredients_count(self, driver, count_ingr=2):
        main_page = actions.get_main_page(driver)
        main_page.add_some_ingredients(driver, count_ingr)
        result = main_page.ingr_count.text
        assert result == str(count_ingr), f'Ошибка: не отработал счетчик ингредиента, {result} вместо {count_ingr}'

    @allure.title('Успешное оформление заказа')
    @allure.description('залогиненный пользователь может оформить заказ')
    def test_create_order_success(self, driver, user):
        main_page = actions.login_and_set_burger(driver, user)
        assert main_page.order_msg_panel.is_displayed(), f'Ошибка: нет формы с деталями заказа после оформления'

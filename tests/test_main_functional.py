import allure

from pages.main_page import MainPage
from pages.orders_ribbon_page import RibbonPage


@allure.feature('Проверка основного функционала')
class TestMainFunctional:

    @allure.title('Переход в «Конструктор»')
    @allure.description('переход по клику на «Конструктор»')
    def test_go_to_constructor(self, driver):
        ribbon_page = RibbonPage(driver)
        ribbon_page.open(ribbon_page.url)
        main_page = MainPage(driver)
        main_page.click_constructor()
        main_page.check_main_page()

    @allure.title('Переход в «Лента заказов»')
    @allure.description('переход по клику на «Лента заказов»')
    def test_go_to_orders_ribbon(self, driver):
        main_page = MainPage(driver)
        main_page.open(main_page.url)
        main_page.click_orders_ribbon()
        ribbon_page = RibbonPage(driver)
        ribbon_page.check_orders_ribbon_page()

    @allure.title('Детали ингредиента')
    @allure.description('если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_get_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.open(main_page.url)
        main_page.click_ingredient()
        main_page.check_ingr_details_form()

    @allure.title('Детали ингредиента закрываются по крестику')
    @allure.description('всплывающее окно формы "Детали ингредиента" закрывается кликом по крестику')
    def test_close_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.open(main_page.url)
        main_page.click_ingredient()
        main_page.click_cross_btn()
        main_page.check_main_page()

    @allure.title('Счетчик ингредиента')
    @allure.description('при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_ingredients_count(self, driver, count_ingr=2):
        main_page = MainPage(driver)
        main_page.open(main_page.url)
        main_page.add_some_ingredients(driver, count_ingr)
        result = main_page.get_ingr_count()
        assert result == str(count_ingr), f'Ошибка: не отработал счетчик ингредиента, {result} вместо {count_ingr}'

    @allure.title('Успешное оформление заказа')
    @allure.description('залогиненный пользователь может оформить заказ')
    def test_create_order_success(self, driver, user, login):
        main_page = MainPage(driver)
        main_page.add_bun(driver)
        main_page.add_ingredient(driver)
        main_page.click_order_btn()
        main_page.check_main_page()

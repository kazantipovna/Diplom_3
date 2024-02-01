import allure

import helpers.user_actions as actions
from pages.orders_ribbon_page import RibbonPage
from locators.orders_ribbon_page_locators import RibbonPageLocators


@allure.feature('Раздел «Лента заказов»')
class TestOrdersRibbon:

    @allure.title('Всплывающее окно с деталями заказа')
    @allure.description('если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_get_orders_details(self, driver):
        orders_ribbon = actions.get_ribbon_page(driver)
        orders_ribbon.click_element(RibbonPageLocators.last_order)
        element_text = orders_ribbon.get_element_text(RibbonPageLocators.order_compound)
        assert 'Cостав' in element_text, f'Ошибка: не отобразилась панель ингредиента'

    @allure.title('Счетчик Выполнено за всё время')
    @allure.description('при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_counter_all(self, driver, user):
        all_orders = RibbonPage(driver).get_all_orders_count()
        actions.login_and_set_burger(driver, user)
        all_orders_after_order = RibbonPage(driver).get_all_orders_count()
        exp_res = all_orders + 1
        assert all_orders_after_order == exp_res, f'Ошибка: не изменился общий счетчик заказов после заказа'

    @allure.title('Счетчик Выполнено за сегодня')
    @allure.description('при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_counter_today(self, driver, user):
        today_orders = RibbonPage(driver).get_today_orders_count()
        actions.login_and_set_burger(driver, user)
        today_orders_after_order = RibbonPage(driver).get_today_orders_count()
        exp_res = today_orders + 1
        assert today_orders_after_order == exp_res, f'Ошибка: не изменился дневной счетчик заказов после заказа'

    @allure.title('Заказ В работе')
    @allure.description('после оформления заказа его номер появляется в разделе В работе')
    def test_order_in_work(self, driver, user):
        order_number = actions.create_burger_and_get_order_id(driver, user)
        orders_in_work = RibbonPage(driver).get_orders_in_work()
        assert order_number in orders_in_work, \
            f'Ошибка: номер заказа {order_number} отсутствует в списке заказов в работе {orders_in_work}'

    @allure.title('Заказы пользователя')
    @allure.description('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_users_order_in_ribbon(self, driver, user):
        order_number = actions.create_burger_and_get_order_id(driver, user)
        orders_done = RibbonPage(driver).get_orders_done()
        assert order_number in orders_done, \
            f'Ошибка: номер заказа {order_number} отсутствует в списке заказов {orders_done}'

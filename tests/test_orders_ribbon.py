import allure

from pages.main_page import MainPage
from pages.orders_ribbon_page import RibbonPage


@allure.feature('Раздел «Лента заказов»')
class TestOrdersRibbon:

    @allure.title('Всплывающее окно с деталями заказа')
    @allure.description('если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_get_orders_details(self, driver):
        ribbon_page = RibbonPage(driver)
        ribbon_page.open(ribbon_page.url)
        ribbon_page.click_last_order()
        ribbon_page.check_order_compound()

    @allure.title('Счетчик Выполнено за всё время')
    @allure.description('при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_counter_all(self, driver, user, login):
        main_page = MainPage(driver)
        main_page.click_orders_ribbon()
        orders_ribbon = RibbonPage(driver)
        all_orders = orders_ribbon.get_all_orders_count()
        main_page.create_burger(driver)
        main_page.click_orders_ribbon()
        all_orders_after_order = RibbonPage(driver).get_all_orders_count()
        exp_res = all_orders + 1
        assert all_orders_after_order == exp_res, f'Ошибка: не изменился общий счетчик заказов после заказа'

    @allure.title('Счетчик Выполнено за сегодня')
    @allure.description('при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_counter_today(self, driver, user, login):
        main_page = MainPage(driver)
        main_page.click_orders_ribbon()
        orders_ribbon = RibbonPage(driver)
        today_orders = orders_ribbon.get_today_orders_count()
        main_page.create_burger(driver)
        main_page.click_orders_ribbon()
        today_orders_after_order = orders_ribbon.get_today_orders_count()
        exp_res = today_orders + 1
        assert today_orders_after_order == exp_res, f'Ошибка: не изменился дневной счетчик заказов после заказа'

    @allure.title('Заказ В работе')
    @allure.description('после оформления заказа его номер появляется в разделе В работе')
    def test_order_in_work(self, driver, user, login):
        main_page = MainPage(driver)
        order_number = main_page.create_burger(driver)
        ribbon_page = RibbonPage(driver)
        orders_in_work = ribbon_page.get_orders_in_work()
        assert order_number in orders_in_work, \
            f'Ошибка: номер заказа {order_number} отсутствует в списке заказов в работе {orders_in_work}'

    @allure.title('Заказы пользователя')
    @allure.description('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_users_order_in_ribbon(self, driver, user, login):
        main_page = MainPage(driver)
        order_number = main_page.create_burger(driver)
        ribbon_page = RibbonPage(driver)
        orders_done = ribbon_page.get_orders_done()
        assert order_number in orders_done, \
            f'Ошибка: номер заказа {order_number} отсутствует в списке заказов {orders_done}'

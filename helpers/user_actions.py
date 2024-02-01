
import allure

from pages.lk_page import LkPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from pages.orders_ribbon_page import RibbonPage
from pages.recover_page import RecoverPage


def get_login_page(driver):
    login_page = LoginPage(driver)
    login_page.open(login_page.url)
    return login_page


def get_recovery_page(driver):
    recovery_page = RecoverPage(driver)
    recovery_page.open(recovery_page.url)
    return recovery_page


def get_main_page(driver):
    main_page = MainPage(driver)
    main_page.open(main_page.url)
    return main_page


def get_ribbon_page(driver):
    ribbon_page = RibbonPage(driver)
    ribbon_page.open(ribbon_page.url)
    return ribbon_page


def login(driver, user):
    login_page = get_login_page(driver)
    login_page.login_fields_set(user)


def login_and_go_to_lk(driver, user):
    login(driver, user)
    lk = LkPage(driver)
    lk.lk_btn_click()
    return lk


def recovery_page_set_email(driver, user):
    recovery_page = get_recovery_page(driver)
    recovery_page.recover_set_email(user)
    return recovery_page


def get_ingredient_form(driver):
    main_page = get_main_page(driver)
    main_page.click_element(MainPageLocators.ingredient)
    return main_page


@allure.step('Создаем бургер')
def login_and_set_burger(driver, user):
    login(driver, user)
    main_page = MainPage(driver)
    main_page.add_bun(driver)
    main_page.add_ingredient(driver)
    main_page.click_element(MainPageLocators.order_btn)
    return main_page


@allure.step('Получаем номер заказа')
def create_burger_and_get_order_id(driver, user):
    main_page = login_and_set_burger(driver, user)
    main_page.wait_for_element_invisibility(main_page.locators.default_order_number)
    order_number = main_page.get_order_number()
    return order_number

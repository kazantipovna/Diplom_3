from time import sleep

import allure

from pages.history_page import HistoryPage
from pages.lk_page import LkPage
from pages.login_page import LoginPage
from pages.main_page import MainPage

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


def login_and_go_to_lk(driver, user):
    login(driver, user)
    main_page = MainPage(driver)

    with allure.step('Переходим в ЛК'):
        main_page.click_web_element(main_page.lk_btn)
        lk_page = LkPage(driver)
        lk_page.lk_profile.is_displayed()
        return lk_page


def get_main_page(driver):
    main_page = MainPage(driver)
    main_page.open(main_page.url)
    return main_page


def get_ingredient_form(driver):
    main_page = get_main_page(driver)
    main_page.click_web_element(main_page.ingredient)
    return main_page


def login(driver, user):
    with allure.step('Логиним пользователя'):
        login_page = LoginPage(driver)
        login_page.open(login_page.url)
        login_page.click_web_element(login_page.email_fieldset)
        login_page.email_fieldset.send_keys(user['email'])
        login_page.click_web_element(login_page.pass_fieldset)
        login_page.pass_fieldset.send_keys(user['password'])
        login_page.click_web_element(login_page.login_btn)
        return login_page


def login_and_set_burger(driver, user):
    login(driver, user)
    with allure.step('Создаем бургер'):
        main_page = MainPage(driver)
        main_page.add_bun(driver)
        main_page.add_ingredient(driver)
        main_page.click_web_element(main_page.order_btn)
        return main_page


def create_burger_and_get_order_id(driver, user):
    main_page = login_and_set_burger(driver, user)
    with allure.step('Получаем номер заказа'):
        main_page.wait_for_element_invisibility(main_page.locators.default_order_number)
        order_number = str(main_page.get_order_number_text())
        return order_number

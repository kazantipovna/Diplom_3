from time import sleep

import allure

from pages.lk_page import LkPage
from pages.login_page import LoginPage
from pages.main_page import MainPage

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


def login_and_go_to_lk(driver, user):
    """Логинится и заходит в ЛК"""
    login(driver, user)
    main_page = MainPage(driver)

    with allure.step('Переходим в ЛК'):
        main_page.click_web_element(main_page.lk_btn)
        lk_page = LkPage(driver)
        lk_page.lk_profile.is_displayed()
        return lk_page


def get_main_page(driver):
    """Создает объект основной страницы и открывает ее"""
    main_page = MainPage(driver)
    main_page.open(main_page.url)
    return main_page


def get_ingredient_form(driver):
    """Получает формочку ингредиента"""
    main_page = get_main_page(driver)
    main_page.click_web_element(main_page.ingredient)
    return main_page


def login(driver, user):
    """Логинит пользователя"""
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
    """Логинит пользователя и создает бургер"""
    login(driver, user)
    with allure.step('Создаем бургер'):
        main_page = MainPage(driver)
        main_page.add_bun(driver)
        main_page.add_ingredient(driver)
        main_page.click_web_element(main_page.order_btn)
        return main_page


def create_burger_and_get_order_id(driver, user):
    """Создает бургер и получает id заказа залогиненного пользователя"""
    main_page = login_and_set_burger(driver, user)
    with allure.step('Получаем номер заказа'):
        # locator = By.XPATH, '//div/h2[contains(@class,"Modal_modal__title_shadow")]'
        # WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element(locator, '8888'))
        # main_page.wait_for_element_is_visible(main_page.order_number())
        sleep(2) # пришлось оставить самый элементарный слип, иначе в мозиле все наглухо зависает
        order_number = str(main_page.get_order_number_text())
        return order_number

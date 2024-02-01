import allure

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import urls


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = urls.main_url

    @allure.step('Получаем элемент {locator}')
    def get_web_element(self, locator):
        element = self.wait_for_element_is_visible(locator)
        self.scroll_to_web_element(element)
        return self.driver.find_element(*locator)

    @allure.step('Ждем элемент {locator}')
    def wait_for_element_is_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Скроллим до элемента {web_element}')
    def scroll_to_web_element(self, web_element):
        self.driver.execute_script('arguments[0].scrollIntoView();', web_element)

    @allure.step('Кликаем элемент {locator}')
    def click_element(self, locator):
        self.get_web_element(locator).click()

    @allure.step('Вводим текст в поле {locator}')
    def get_element_put_text(self, locator, text):
        self.get_web_element(locator)
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Получаем текст элемента для ассерта {locator}')
    def get_element_text(self, locator):
        return self.get_web_element(locator).text

    @allure.step('Получаем ссылку странички')
    def get_curr_url(self):
        curr_url = self.driver.current_url
        return curr_url

    @allure.step('Открываем страничку {url}')
    def open(self, url):
        self.driver.get(url)

    @allure.step('Ждем скрытия элемента {locator}')
    def wait_for_element_invisibility(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element(locator))

    @allure.step('Получаем название класса для проверки активности поля')
    def get_class_name(self, locator):
        return self.wait_for_element_is_visible(locator).get_attribute("class")

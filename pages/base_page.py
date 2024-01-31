from time import sleep

import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import urls


class BasePage:
    """Класс базовой наследуемой страницы"""

    def __init__(self, driver):
        self.driver = driver
        self.url = urls.main_url

    @allure.step('Открываем страничку {url}')
    def open(self, url):
        self.driver.get(url)

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

    @staticmethod
    def click_web_element(web_element: WebElement, attempts_count: int = 10, attempts_timeout: float = 0.3):
        """
        Повторно кликает в элемент страницы, пока не кликнет успешно, иначе, через attempts_timeout,
         выдаст последнюю ошибку
        :param web_element: WebElement - вэб-элемент
        :param attempts_count: int - количество попыток
        :param attempts_timeout: float - таймаут между попытками
        :return: None
        """
        for i in range(attempts_count):
            try:
                web_element.click()
                break
            except Exception as last_exception:
                sleep(attempts_timeout)
                if i == attempts_count - 1:
                    raise last_exception

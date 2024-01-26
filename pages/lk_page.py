from selenium.webdriver.common.by import By

from pages.base_page import BasePage
import urls


class LkPageLocators:
    """Класс локаторов"""
    lk_profile = By.XPATH, './/a[text()="Профиль"]'
    lk_history = By.XPATH, './/a[text()="История заказов"]'
    lk_exit = By.XPATH, './/button[text()="Выход"]'


class LkPage(BasePage):
    """Класс страницы личного кабинета"""

    def __init__(self, driver):
        super().__init__(driver)
        self.url = urls.lk_profile_url
        self.locators = LkPageLocators()

    @property
    def lk_profile(self):
        return self.get_web_element(self.locators.lk_profile)

    @property
    def lk_history(self):
        return self.get_web_element(self.locators.lk_history)

    @property
    def lk_exit(self):
        return self.get_web_element(self.locators.lk_exit)

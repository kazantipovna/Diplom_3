import allure

from locators.lk_page_locators import LkPageLocators
from pages.base_page import BasePage
import urls


class LkPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = urls.lk_profile_url
        self.locators = LkPageLocators()

    @allure.step('Кликаем кнопку "Личный кабинет"')
    def lk_btn_click(self):
        self.click_element(self.locators.lk_btn)

    @allure.step('Кликаем кнопку "Выход"')
    def lk_exit_click(self):
        self.click_element(self.locators.lk_exit)

from pages.base_page import BasePage
import urls


class HistoryPageLocators:
    """Класс локаторов"""
    pass


class HistoryPage(BasePage):
    """Класс страницы истории в личном кабинете"""

    def __init__(self, driver):
        super().__init__(driver)
        self.url = urls.lk_history_url
        self.locators = HistoryPageLocators()


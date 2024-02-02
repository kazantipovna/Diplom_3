import allure

from pages.base_page import BasePage
import urls


class HistoryPage(BasePage):
    """Класс страницы истории в личном кабинете"""

    def __init__(self, driver):
        super().__init__(driver)
        self.url = urls.lk_history_url

    @allure.step('Проверяем, что страничка истории заказов пользователя загрузилась')
    def check_history_url(self):
        curr_url = self.get_curr_url()
        assert curr_url == urls.lk_history_url, f'Ошибка: не осуществлен переход в п/м «История заказов»'

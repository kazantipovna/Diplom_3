from selenium.webdriver.common.by import By


class LkPageLocators:
    lk_profile = By.XPATH, './/a[text()="Профиль"]'
    lk_history = By.XPATH, './/a[text()="История заказов"]'
    lk_exit = By.XPATH, './/button[text()="Выход"]'
    lk_btn = By.XPATH, './/p[text()="Личный Кабинет"]'

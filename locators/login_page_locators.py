from selenium.webdriver.common.by import By


class LoginPageLocators:
    recover_pass = By.XPATH, './/a[text()="Восстановить пароль"]'
    login_btn = By.XPATH, './/button[text()="Войти"]'
    email_fieldset = By.XPATH, './/input[@name="name"]'
    pass_fieldset = By.XPATH, './/input[@name="Пароль"]'
    header_enter = By.XPATH, './/h2[text()="Вход"]'
    # header_recover = By.XPATH, './/h2[text()="Восстановление пароля"]'

from selenium.webdriver.common.by import By


class RecoverPageLocators:
    recover_pass_btn = By.XPATH, './/button[text()="Восстановить"]'
    header_h2 = By.XPATH, './/h2'  # любой заголовок h2
    email_field = By.XPATH, '//input[@name="name"]'
    save_btn = By.XPATH, './/button[text()="Сохранить"]'
    eye_btn = By.CLASS_NAME, 'input__icon'
    recover_pass_set = By.XPATH, './/label[text()="Пароль"]'
    header_recover = By.XPATH, './/h2[text()="Восстановление пароля"]'

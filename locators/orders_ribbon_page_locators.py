from selenium.webdriver.common.by import By


class RibbonPageLocators:
    orders_ribbon_header = By.XPATH, './/h1[text()="Лента заказов"]'
    last_order = By.XPATH, './/div[contains(@class,"OrderHistory_dataBox__1mkxK")]'
    order_panel = By.XPATH, './/div[contains(@class,"Modal_orderBox__1xWdi")]'
    all_orders = By.XPATH, './/div[2]/p[contains(@class,"OrderFeed_number__2MbrQ")]'
    today_orders = By.XPATH, './/div[3]/p[contains(@class,"OrderFeed_number__2MbrQ")]'
    orders_in_work = By.XPATH, './/ul[2]/li[contains(@class,"text text_type_digits-default")]'
    orders_done = By.XPATH, './/div[1]/ul[1][contains(@class,"OrderFeed_orderList")]'
    order_compound = By.XPATH, './/div/p[3][text()="Cостав"]'

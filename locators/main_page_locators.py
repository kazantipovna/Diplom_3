from selenium.webdriver.common.by import By


class MainPageLocators:
    order_btn = By.XPATH, './/button[text()="Оформить заказ"]'
    lk_btn = By.XPATH, './/p[text()="Личный Кабинет"]'
    constructor = By.XPATH, './/p[text()="Конструктор"]'
    orders_ribbon = By.XPATH, './/p[text()="Лента Заказов"]'
    create_burger_header = By.XPATH, './/h1[text()="Соберите бургер"]'
    ingredient = By.XPATH, './/ul[3]/a[1]/img[contains(@class,"BurgerIngredient_ingredient")]'
    ingr_text = By.XPATH, './/div/h2[text()="Детали ингредиента"]'
    ingr_count = By.XPATH, './/ul[3]/a[1]/div[1]/p[contains(@class,"counter_counter")]'
    bun = By.XPATH, './/ul[1]/a[1]/img[contains(@class,"BurgerIngredient_ingredient")]'
    ingredient_details = By.XPATH, './/h2[text()="Детали ингредиента"]'
    cross_btn = By.XPATH, './/button[@type="button"]'
    burger_constructor_basket = By.XPATH, './/ul[contains(@class,"BurgerConstructor_basket")]'
    order_msg_panel = By.XPATH, '//div[contains(@class,"Modal_modal__contentBox__sCy8X")]'
    order_number = By.XPATH, '//div/h2[contains(@class,"Modal_modal__title_shadow")]'
    default_order_number = By.XPATH, '//div/h2[text()="9999"]'

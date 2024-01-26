
from selenium.webdriver.common.by import By


class AllLocators:
# MyOld
    LOGIN_BNT1 = By.XPATH, './/button[text()="Войти в аккаунт"]'  # кнопка "Войти в аккаунт" с главной
    LOGIN_BNT2 = By.XPATH, './/button[text()="Войти"]'  # кнопка "Войти" со странички входа
    LOGIN_H2 = By.XPATH, './/h2[text()="Вход"]'  # заголовок "Вход"
    LOGIN_A = By.XPATH, './/a[text()="Войти"]'  # ссылка "Войти" из восстановления пароля
    LOGOUT_BNT = By.XPATH, './/button[text()="Выход"]'  # кнопка "Выход"
    LK_BNT = By.XPATH, './/p[text()="Личный Кабинет"]'  # меню "Личный кабинет"
    REGISTER_BNT = By.XPATH, './/button[text()="Зарегистрироваться"]'  # кнопка "Зарегистрироваться"
    RECOVER_PASS = By.XPATH, './/a[text()="Восстановить пароль"]'  # пункт "Восстановить пароль"
    RECOVER_PASS_BNT = By.XPATH, './/button[text()="Восстановить"]'  # кнопка "Восстановить пароль"
    LK_PROFILE = By.XPATH, './/a[text()="Профиль"]'  # меню "Профиль" в ЛК
    INCORRECT_PASS = By.XPATH, './/fieldset[3]/div/p[text()="Некорректный пароль"]'  # сообщение "Некорректный пароль"
    INCORRECT_PASS_CHECK = By.XPATH, './/fieldset[3]/div/p'  # для проверки сообщения "Некорректный пароль"
    USER_EXISTS = By.XPATH, './/div/main/div/p[text()="Такой пользователь уже существует"]'  # сообщение "Такой пользователь уже существует"
    USER_EXISTS_CHECK = By.XPATH, './/div/main/div/p'  # для проверки сообщения "Такой пользователь уже существует"
    FIELDSET1 = By.XPATH, './/fieldset[1]//input'  # поле для ввода данных
    FIELDSET2 = By.XPATH, './/fieldset[2]//input'  # поле для ввода данных
    FIELDSET3 = By.XPATH, './/fieldset[3]//input'  # поле для ввода данных
    HEADER_H2 = By.XPATH, './/h2'  # любой заголовок h2
    MAKE_BURGER = By.XPATH, './/section[1]/h1[text()="Соберите бургер"]'  # заголовок "Соберите бургер" в конструкторе
    CONSTRUCTOR = By.XPATH, './/p[text()="Конструктор"]'  # меню "Конструктор"
    ORDER_BNT = By.XPATH, './/button[text()="Оформить заказ"]'  # кнопка "Оформить заказ"
    SOUSES = By.XPATH, './/span[text()="Соусы"]'  # меню "Соусы"
    NACHINKI = By.XPATH, './/span[text()="Начинки"]'  # список "Соусы"
    BULKI = By.XPATH, './/span[text()="Булки"]'  # меню "Булки"
    SOUSES_CHECK = By.XPATH, './/h2[text()="Соусы"]'  # список "Булки"
    NACHINKI_CHECK = By.XPATH, './/h2[text()="Начинки"]'  # меню "Начинки"
    BULKI_CHECK = By.XPATH, './/h2[text()="Начинки"]'  # список "Начинки"


# LoginPageLocators
    LOCATOR_EMAIL_INPUT_LOGIN_PAGE = (By.XPATH, "//input[@name='name']")  # поле для ввода емайла на странице авторизации
    LOCAROR_PASSWORD_INPUT_LOGIN_PAGE = (By.XPATH, "//input[@name='Пароль']")  # поле для ввода пароля на странице авторизации
    LOCATOR_LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")  # кнопка входа на странице авторизации
    LOCATOR_TEXT_PASSWORD_RECOVERY_ON_HEADER = By.XPATH, "//h2[contains(text(),'Восстановление пароля')]"
    LOCATOR_FORGOT_PASSWORD_BATTON = By.XPATH, "//a[contains(text(),'Восстановить пароль')]"
    LOCATOR_RECOVER_BTN = By.XPATH, "//button[contains(text(),'Восстановить')]"
    LOCATOR_INPUT_EMAIL = By.XPATH, "//input[@name='name']"
    LOCATOR_INPUT_PASSWORD = By.XPATH, "//input[@name='//input[@name='Введите новый пароль']']"
    LOCATOR_INPUT_CODE = By.XPATH, "//input[@name='//input[@name='name']']"
    LOCATOR_SAVE_BTN = By.XPATH, "//button[contains(text(),'Сохранить')]"
    LOCATOR_EYE_ICON = By.XPATH, "//div[contains(@class,'input__icon-action')]"
    LOCATOR_LOGIN_TEXT_ON_HEADER = By.XPATH, "//h2[contains(text(),'Вход')]"
    LOCATOR_ACTIVE_PASSWORD_INPUT = By.XPATH, "//label[contains(@class,'input__placeholder text noselect')][1]"

# MainPageLocators:
    LOCATOR_PROFILE_BATTON_ON_HEADER = By.XPATH, "//p[contains(text(),'Личный Кабинет')]"
    LOCATOR_CONSTRUCTOR_BTN_ON_HEADER = By.XPATH, "//p[contains(text(),'Конструктор')]"
    LOCATOR_FEED_BTN = By.XPATH, "//p[contains(text(),'Лента Заказов')]"
    LOCATOR_BURGER_TITLE_ON_MAIN = By.XPATH, "//h1[text()='Соберите бургер']"
    LOCATOR_INGREDIENT_BTN = By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]"
    LOCATOR_TEXT_ON_DETAIL_MODAL = By.XPATH, "//h2[contains(text(),'Детали ингредиента')]"
    LOCATOR_CLOSE_DETAIL_INGREDIENT_MODAL = By.XPATH, "//button[contains(@class, 'Modal_modal__close')]"
    LOCATOR_CREATE_ORDER = By.XPATH, "//button[contains(text(),'Оформить заказ')]"
    LOCATOR_CONFIRM_CREATE_ORDER = By.XPATH, "//p[contains(text(),'Ваш заказ начали готовить')]"
    LOCATOR_INGREDIENT_BUN = By.XPATH, "//a[contains(@class, 'BurgerIngredient')]"
    LOCATOR_BURGER_CONSTRUCTOR = By.XPATH, "//ul[@class = 'BurgerConstructor_basket__list__l9dp_']"
    LOCATOR_ACTIVE_COUNTER_ON_BUN = By.XPATH, "//div[@class='counter_counter__ZNLkj counter_default__28sqi']/p[text()='2'][1]"
    LOCATOR_ORDER_NUMBER_ON_MODAL = By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]"

# FeedOrderPageLocators:
    LOCATOR_FEED_TEXT_ON_HEADER = By.XPATH, "//h1[contains(text(),'Лента заказов')]"
    LOCATOR_ORDER_LIST_BTN = By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]"
    LOCATOR_TEXT_ON_DETAILS_ORDER_MODAL = By.XPATH, "//p[contains(text(),'Cостав')]"
    LOCATOR_ORDER_NUMBER_ON_ORDER_FEED = By.XPATH, "//p[@class = 'text text_type_digits-default']"
    LOCATOR_ALL_TIME_COUNTER = By.XPATH, "//p[contains(text(),'Выполнено за все время')]/following-sibling::p[contains(@class, 'OrderFeed_number')]"
    LOCATOR_DAY_TIME_COUNTER = By.XPATH, "//p[contains(text(),'Выполнено за сегодня')]/following-sibling::p[contains(@class, 'OrderFeed_number')]"
    LOCATOR_ORDER_LIST_STATUS_IN_WORKING = By.XPATH, "//*[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']"

# ProfilePageLocators:
    LOCATOR_PROFILE_TEXT = By.XPATH, "//a[contains(text(),'Профиль')]"
    LOCATOR_LOGOUT = By.XPATH, "//button[contains(text(),'Выход')]"
    LOCATOR_ORDER_HISTORY_BTN = By.XPATH, "//a[contains(text(),'История заказов')]"
    LOCATOR_LIST_ORDER_HISTORY = By.XPATH, "//div[@class ='OrderHistory_orderHistory__qy1VB']"
    LOCATOR_ORDER_NUMBER_ON_HISTORY_ORDER = By.XPATH, "//p[@class = 'text text_type_digits-default']"


# def test_order_in_work(self, driver, attempts_count: int = 10, attempts_timeout: float = 0.3):
#     main_page = helpers.login_and_set_burger(driver)
#
#     for i in range(attempts_count):
#         while str(main_page.get_order_number_text()) == '9999':
#             sleep(attempts_timeout)
#         else:
#             order_number = str(main_page.get_order_number_text())
#
#     orders_in_work = str(RibbonPage(driver).get_orders_in_work())
#
#     if order_number not in orders_in_work:
#         for j in range(attempts_count):
#             sleep(attempts_timeout)
#             orders_in_work = str(RibbonPage(driver).get_orders_in_work())
#
#     assert order_number in orders_in_work


#
# def create_burger_and_get_order_id(driver, user, attempts_timeout: float = 0.3):
#     """Создает бургер и получает id заказа залогиненного пользователя"""
#     main_page = login_and_set_burger(driver, user)
#     with allure.step(f'Получаем номер заказа'):
#         sleep(attempts_timeout)
#         order_number = str(main_page.get_order_number_text())
#         return order_number
#
#         # while str(main_page.get_order_number_text()) == '9999':
#         #     sleep(attempts_timeout)
#         # else:
#         #     order_number = str(main_page.get_order_number_text())
#         # return order_number

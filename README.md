## Дипломный проект. Задание 3: WEB-тесты

---
#### Тесты на проверку WEB учебного сервиса "Stellar Burgers" https://stellarburgers.nomoreparties.site/
___

### Каталог pages:
* `base_page.py` - описание базовой страницы
* `lk_page.py` - страница личного кабинета
* `login_page.py` - страница логина пользователя
* `main_page.py` - главная страница (конструктор)
* `orders_ribbon_page.py` - страница с лентой заказов
* `recover_page.py` - страница восстановления пароля
* `history_page.py` - страница ленты заказов

### Каталог locators:
* `lk_page_locators.py` - локаторы страницы личного кабинета
* `login_page_locators.py` - локаторы страницы логина пользователя
* `main_page_locators.py` - локаторы главной страницы (конструктор)
* `orders_ribbon_page_locators.py` - локаторы страницы с лентой заказов
* `recover_page.py_locators` - локаторы страницы восстановления пароля

### Каталог tests:
* `test_lk.py` - тесты по ЛК:
  * **Тесты:**
    * test_go_to_lk - Переход в «Личный кабинет»
    * test_go_to_orders_history - Переход в «История заказов»
    * test_logout - Выход из аккаунта


* `test_main_functional.py` - Проверка основного функционала:
  * **Тесты:**
    * test_go_to_constructor - Переход в «Конструктор»
    * test_go_to_orders_ribbon - Переход в «Лента заказов»
    * test_get_ingredient_details - Детали ингредиента
    * test_close_ingredient_details - Детали ингредиента закрываются по крестику
    * test_ingredients_count - Счетчик ингредиента
    * test_create_order_success - Успешное оформление заказа


* `test_order_ribbon.py` - тесты ленты заказов:
  * **Тесты:**
    * test_get_orders_details - Всплывающее окно с деталями заказа
    * test_counter_all - Счетчик Выполнено за всё время
    * test_counter_today - Счетчик Выполнено за сегодня
    * test_order_in_work - Заказ В работе
    * test_users_order_in_ribbon - Заказы пользователя


* `test_recovers.py` - тесты кнопок по восстановлению пароля:
  * **Тесты:**
    * test_go_to_recover - Кнопка «Восстановить пароль»
    * test_recover_fill_email_field - Ввод почты для восстановления
    * test_recover_btn_click - Кнопка «Восстановить»
    * test_recover_pass_field_active - Кнопка "показать/скрыть пароль"


* `helpers.py` - методы по созданию и удалению тестового пользователя
* `conftest.py` - фикстуры
* `urls.py` - ссылки

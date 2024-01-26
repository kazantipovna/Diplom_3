import pytest
from selenium import webdriver

import helpers.user_create as new_user

# путь до драйверов
DRIVER_PATH_CHROME = './chromedriver'
DRIVER_PATH_FIREFOX = './geckodriver'


@pytest.fixture(params=['firefox', 'chrome'], scope='function')
def driver(request):
    driver = None
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    if request.param == 'firefox':
        driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture
def user(driver):
    """Фикстура пользователя, создает и удаляет пользака для теста"""
    user = new_user.register_new_user()
    yield user
    new_user.delete_user(user)

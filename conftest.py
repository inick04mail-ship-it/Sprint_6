import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture
@allure.title("Подготовка драйвера Firefox")
def driver():
    options = Options()
   

    with allure.step("Запуск браузера Firefox"):
        browser = webdriver.Firefox(options=options)
        browser.maximize_window()

    yield browser

    with allure.step("Закрытие браузера Firefox"):
        browser.quit()

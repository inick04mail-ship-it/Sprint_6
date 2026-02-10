import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть URL: {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Клик по элементу: {locator}")
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    @allure.step("Найти элемент: {locator}")
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Ожидать видимость элемента: {locator}")
    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Прокрутить к элементу")
    def scroll_into_view(self, element):
        """Прокручивает страницу так, чтобы элемент был виден."""
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Проверить наличие элемента: {locator}")
    def is_element_present(self, locator, timeout: int = 3) -> bool:
        """Проверяет наличие элемента без выбрасывания исключения."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

  
    @allure.step("Получить текущий дескриптор окна")
    def get_current_window_handle(self):
        return self.driver.current_window_handle

    @allure.step("Получить список всех окон")
    def get_window_handles(self):
        return self.driver.window_handles

    @allure.step("Переключиться в окно: {handle}")
    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def scroll_into_view(self, element):
        """Прокручивает страницу так, чтобы элемент был виден."""
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    # --- Работа с окнами/вкладками ---

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def get_window_handles(self):
        return self.driver.window_handles

    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)

    def get_current_url(self):
        return self.driver.current_url

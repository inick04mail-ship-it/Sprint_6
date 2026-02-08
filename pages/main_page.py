from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from .base_page import BasePage
from urls import BASE_URL


class MainPageLocators:
    # Кнопка «Заказать» вверху страницы
    ORDER_BUTTON_TOP = (By.CLASS_NAME, "Button_Button__ra12g")

    # Кнопка «Заказать» внизу страницы
    ORDER_BUTTON_BOTTOM = (
        By.XPATH,
        "//div[contains(@class, 'Home_FinishButton')]/button",
    )

    # Кнопка согласия с куками (если есть баннер)
    COOKIE_ACCEPT_BUTTON = (By.ID, "rcc-confirm-button")

    # Логотип Самоката
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")

    # Логотип Яндекса
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    # FAQ
    @staticmethod
    def question_locator(index: int):
        return (By.ID, f"accordion__heading-{index}")

    @staticmethod
    def answer_locator(index: int):
        return (By.ID, f"accordion__panel-{index}")


class MainPage(BasePage):
    """Page Object главной страницы «Яндекс.Самокат»."""

    def open_main_page(self):
        self.open(BASE_URL)

    def accept_cookies_if_present(self):
        try:
            self.click(MainPageLocators.COOKIE_ACCEPT_BUTTON)
        except TimeoutException:
            pass

    def click_order_top(self):
        self.accept_cookies_if_present()
        self.click(MainPageLocators.ORDER_BUTTON_TOP)

    def click_order_bottom(self):
        self.accept_cookies_if_present()
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    # FAQ

    def click_question(self, index: int):
        question = self.find(MainPageLocators.question_locator(index))
        self.scroll_into_view(question)
        self.click(MainPageLocators.question_locator(index))

    def get_answer_text(self, index: int) -> str:
        answer = self.is_visible(MainPageLocators.answer_locator(index))
        return answer.text

    # Логотипы

    def click_scooter_logo(self):
        """Кликает по логотипу Самоката."""
        self.click(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        """Кликает по логотипу Яндекса."""
        self.click(MainPageLocators.YANDEX_LOGO)

    def get_yandex_logo_href(self) -> str:
        """Возвращает href логотипа Яндекса."""
        logo = self.find(MainPageLocators.YANDEX_LOGO)
        return logo.get_attribute("href")

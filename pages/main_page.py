import allure
from selenium.webdriver.common.by import By

from .base_page import BasePage
from urls import BASE_URL


class MainPageLocators:
    ORDER_BUTTON_TOP = (By.CLASS_NAME, "Button_Button__ra12g")

    ORDER_BUTTON_BOTTOM = (
        By.XPATH,
        "//div[contains(@class, 'Home_FinishButton')]/button",
    )

    COOKIE_ACCEPT_BUTTON = (By.ID, "rcc-confirm-button")

   
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")

   
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    
    @staticmethod
    def question_locator(index: int):
        return (By.ID, f"accordion__heading-{index}")

    @staticmethod
    def answer_locator(index: int):
        return (By.ID, f"accordion__panel-{index}")


class MainPage(BasePage):
    """Page Object главной страницы «Яндекс.Самокат»."""

    @allure.step("Открыть главную страницу Самоката")
    def open_main_page(self):
        self.open(BASE_URL)

    @allure.step("Принять куки, если баннер отображается")
    def accept_cookies_if_present(self):
        if self.is_element_present(MainPageLocators.COOKIE_ACCEPT_BUTTON):
            self.click(MainPageLocators.COOKIE_ACCEPT_BUTTON)

    @allure.step("Нажать кнопку 'Заказать' вверху страницы")
    def click_order_top(self):
        self.accept_cookies_if_present()
        self.click(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Нажать кнопку 'Заказать' внизу страницы")
    def click_order_bottom(self):
        self.accept_cookies_if_present()
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    

    @allure.step("Клик по вопросу FAQ с индексом {index}")
    def click_question(self, index: int):
        question = self.find(MainPageLocators.question_locator(index))
        self.scroll_into_view(question)
        self.click(MainPageLocators.question_locator(index))

    @allure.step("Получить текст ответа FAQ с индексом {index}")
    def get_answer_text(self, index: int) -> str:
        answer = self.is_visible(MainPageLocators.answer_locator(index))
        return answer.text

   

    @allure.step("Клик по логотипу Самоката")
    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Клик по логотипу Яндекса")
    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)

    @allure.step("Получить ссылку логотипа Яндекса")
    def get_yandex_logo_href(self) -> str:
        logo = self.find(MainPageLocators.YANDEX_LOGO)
        return logo.get_attribute("href")

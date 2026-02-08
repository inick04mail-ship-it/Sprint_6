from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base_page import BasePage


class OrderPageLocators:
    # Шаг 1: Для кого самокат
    FIRST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTION_FIRST = (By.CSS_SELECTOR, ".select-search__option")
    PHONE_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Телефон: на него позвонит курьер']",
    )
    NEXT_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'Button_Middle') and text()='Далее']",
    )

    # Шаг 2: Про аренду
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    RENT_OPTION_ONE_DAY = (
        By.XPATH,
        "//div[@class='Dropdown-option' and text()='сутки']",
    )
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'Button_Middle') and text()='Заказать']",
    )
    CONFIRM_YES_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'Button_Middle') and text()='Да']",
    )
    ORDER_MODAL_TITLE = (
        By.XPATH,
        "//div[contains(@class,'Order_Modal')]//div[contains(text(),'Заказ оформлен')]",
    )


class OrderPage(BasePage):
    def fill_step_one(self, first_name, last_name, address, metro, phone):
        """Заполняет первый шаг формы заказа."""
        self.find(OrderPageLocators.FIRST_NAME_INPUT).send_keys(first_name)
        self.find(OrderPageLocators.LAST_NAME_INPUT).send_keys(last_name)
        self.find(OrderPageLocators.ADDRESS_INPUT).send_keys(address)

        # Всегда выбираем конкретную станцию, чтобы список был предсказуем
        metro_input = self.find(OrderPageLocators.METRO_INPUT)
        metro_input.click()
        metro_input.clear()
        metro_input.send_keys("Сокольники")

        metro_option = self.find(OrderPageLocators.METRO_OPTION_FIRST)
        metro_option.click()

        phone_input = self.find(OrderPageLocators.PHONE_INPUT)
        phone_input.click()
        phone_input.clear()
        phone_input.send_keys(phone)

        self.click(OrderPageLocators.NEXT_BUTTON)

    def fill_step_two(self, date, rent_period_text, color, comment):
        """Заполняет второй шаг формы заказа."""
        # Дата: вводим и закрываем календарь
        date_input = self.find(OrderPageLocators.DATE_INPUT)
        date_input.click()
        date_input.clear()
        date_input.send_keys(date)
        # закрываем календарь: Enter (или клик вне поля)
        date_input.send_keys(Keys.ENTER)

        # Сейчас всегда выбираем «сутки»
        self.click(OrderPageLocators.RENT_DROPDOWN)
        self.click(OrderPageLocators.RENT_OPTION_ONE_DAY)

        if color == "black":
            self.click(OrderPageLocators.COLOR_BLACK)
        elif color == "grey":
            self.click(OrderPageLocators.COLOR_GREY)

        if comment:
            self.find(OrderPageLocators.COMMENT_INPUT).send_keys(comment)

    def submit_order(self):
        self.click(OrderPageLocators.ORDER_BUTTON)
        self.click(OrderPageLocators.CONFIRM_YES_BUTTON)

    def is_order_created(self) -> bool:
        modal = self.is_visible(OrderPageLocators.ORDER_MODAL_TITLE)
        return modal.is_displayed()

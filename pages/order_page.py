import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base_page import BasePage


class OrderPageLocators:
    
    FIRST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTION_LIST = (By.CSS_SELECTOR, ".select-search__option")
    PHONE_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Телефон: на него позвонит курьер']",
    )
    NEXT_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'Button_Middle') and text()='Далее']",
    )

    
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    RENT_OPTION = (
        By.XPATH,
        "//div[@class='Dropdown-option' and text()='{period}']",
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
    @allure.step(
        "Заполнить шаг 1: {first_name} {last_name}, адрес {address}, метро {metro}, телефон {phone}"
    )
    def fill_step_one(self, first_name, last_name, address, metro, phone):
        """Заполняет первый шаг формы заказа."""
        self.find(OrderPageLocators.FIRST_NAME_INPUT).send_keys(first_name)
        self.find(OrderPageLocators.LAST_NAME_INPUT).send_keys(last_name)
        self.find(OrderPageLocators.ADDRESS_INPUT).send_keys(address)

       
        metro_input = self.find(OrderPageLocators.METRO_INPUT)
        metro_input.click()
        metro_input.clear()
        metro_input.send_keys(metro)

       
        metro_option = self.find(OrderPageLocators.METRO_OPTION_LIST)
        metro_option.click()

        phone_input = self.find(OrderPageLocators.PHONE_INPUT)
        phone_input.click()
        phone_input.clear()
        phone_input.send_keys(phone)

        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step(
        "Заполнить шаг 2: дата {date}, период {rent_period_text}, цвет {color}, комментарий: {comment}"
    )
    def fill_step_two(self, date, rent_period_text, color, comment):
        """Заполняет второй шаг формы заказа."""
        
        date_input = self.find(OrderPageLocators.DATE_INPUT)
        date_input.click()
        date_input.clear()
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)

        self.click(OrderPageLocators.RENT_DROPDOWN)
        rent_locator = (
            OrderPageLocators.RENT_OPTION[0],
            OrderPageLocators.RENT_OPTION[1].format(period=rent_period_text),
        )
        self.click(rent_locator)

        if color == "black":
            self.click(OrderPageLocators.COLOR_BLACK)
        elif color == "grey":
            self.click(OrderPageLocators.COLOR_GREY)

        if comment:
            self.find(OrderPageLocators.COMMENT_INPUT).send_keys(comment)

    @allure.step("Подтвердить оформление заказа")
    def submit_order(self):
        self.click(OrderPageLocators.ORDER_BUTTON)
        self.click(OrderPageLocators.CONFIRM_YES_BUTTON)

    @allure.step("Проверить, что заказ успешно создан")
    def is_order_created(self) -> bool:
        modal = self.is_visible(OrderPageLocators.ORDER_MODAL_TITLE)
        return modal.is_displayed()

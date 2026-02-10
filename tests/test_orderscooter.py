import pytest
import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.order_data import ORDER_TEST_DATA


@allure.title("Успешное оформление заказа самоката ({data[button]} кнопка)")
@pytest.mark.parametrize("data", ORDER_TEST_DATA)
def test_success_order_flow(driver, data):
    main_page = MainPage(driver)
    order_page = OrderPage(driver)

    main_page.open_main_page()

    if data["button"] == "top":
        main_page.click_order_top()
    else:
        main_page.click_order_bottom()

    order_page.fill_step_one(
        data["first_name"],
        data["last_name"],
        data["address"],
        data["metro"],
        data["phone"],
    )

    order_page.fill_step_two(
        data["date"],
        data["rent_period"],
        data["color"],
        data["comment"],
    )

    order_page.submit_order()

    assert order_page.is_order_created(), "Должно появиться окно об успешном создании заказа"

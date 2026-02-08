import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage


order_data = [
    {
        "button": "top",
        "first_name": "Иван",
        "last_name": "Иванов",
        "address": "Москва, Тверская 1",
        "metro": "Любая",
        "phone": "+79990000001",
        "date": "20.02.2026",
        "rent_period": "сутки",
        "color": "black",
        "comment": "Позвоните за час",
    },
    {
        "button": "bottom",
        "first_name": "Анна",
        "last_name": "Петрова",
        "address": "Москва, Арбат 10",
        "metro": "Любая",
        "phone": "+79990000002",
        "date": "21.02.2026",
        "rent_period": "сутки",
        "color": "grey",
        "comment": "",
    },
]


@pytest.mark.parametrize("data", order_data)
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

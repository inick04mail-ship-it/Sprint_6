from selenium.webdriver.support.ui import WebDriverWait

from pages.main_page import MainPage
from pages.order_page import OrderPage
from urls import BASE_URL


def test_logo_scooter_from_order_returns_to_main(driver):
    main_page = MainPage(driver)
    order_page = OrderPage(driver)

    main_page.open_main_page()
    main_page.click_order_top()

    main_page.click_scooter_logo()

    current_url = main_page.get_current_url()
    assert current_url.startswith(BASE_URL)


def test_logo_yandex_opens_dzen_or_new_tab(driver):
    main_page = MainPage(driver)
    order_page = OrderPage(driver)

    main_page.open_main_page()
    main_page.click_order_top()

    # Проверяем, что href у логотипа ведёт на yandex.ru
    href = main_page.get_yandex_logo_href()
    assert "yandex.ru" in href

    original_window = main_page.get_current_window_handle()
    assert len(main_page.get_window_handles()) == 1

    main_page.click_yandex_logo()

    # Ждём появления нового окна (их должно стать больше 1)
    WebDriverWait(driver, 10).until(
        lambda d: len(d.window_handles) > 1
    )

    new_window = None
    for handle in main_page.get_window_handles():
        if handle != original_window:
            new_window = handle
            break

    assert new_window is not None
    main_page.switch_to_window(new_window)

    current_url = main_page.get_current_url()

    if current_url != "about:blank":
        assert "dzen.ru" in current_url or "yandex.ru" in current_url

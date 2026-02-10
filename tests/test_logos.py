import allure
from selenium.webdriver.support.ui import WebDriverWait

from pages.main_page import MainPage
from pages.order_page import OrderPage
from urls import BASE_URL


@allure.title("Переход на главную страницу по логотипу Самоката со страницы заказа")
def test_logo_scooter_from_order_returns_to_main(driver):
    main_page = MainPage(driver)
    order_page = OrderPage(driver)

    main_page.open_main_page()
    main_page.click_order_top()

    main_page.click_scooter_logo()

    current_url = main_page.get_current_url()
    assert current_url.startswith(BASE_URL)


@allure.title("Открытие Dzen/Яндекс в новой вкладке по клику на логотип Яндекса")
def test_logo_yandex_opens_dzen_or_new_tab(driver):
    main_page = MainPage(driver)
    order_page = OrderPage(driver)

    main_page.open_main_page()
    main_page.click_order_top()

    href = main_page.get_yandex_logo_href()
    assert "yandex.ru" in href

    original_window = main_page.get_current_window_handle()
    assert len(main_page.get_window_handles()) == 1

    main_page.click_yandex_logo()

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

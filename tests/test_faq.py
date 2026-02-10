import pytest
import allure

from pages.main_page import MainPage


faq_data = [
    (0, "Сутки — 400 рублей"),
    (1, "Пока что у нас так: один заказ — один самокат"),
    (2, "Допустим, вы оформляете заказ на 8 мая"),
    (3, "Только начиная с завтрашнего дня"),
    (4, "Пока что нет! Но если что-то срочное"),
    (5, "Самокат приезжает к вам с полной зарядкой"),
    (6, "Да, пока самокат не привезли. Штрафа не будет"),
    (7, "Да, обязательно"),
]


@allure.title("Проверка текста ответа FAQ для вопроса №{index}")
@pytest.mark.parametrize("index, expected_text", faq_data)
def test_faq_answer_visible(driver, index, expected_text):
    main_page = MainPage(driver)
    main_page.open_main_page()

    main_page.click_question(index)
    answer_text = main_page.get_answer_text(index)

    assert expected_text in answer_text

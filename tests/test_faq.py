import pytest
import allure
from pages.main_page import MainPage


@allure.feature("FAQ - Вопросы о важном")
class TestFAQ:

    @pytest.mark.parametrize("index", list(range(8)))  # Вопросы 0–7
    @allure.story("Открытие ответа на вопрос из списка")
    def test_faq_question_opens(self, driver, index):
        page = MainPage(driver)
        with allure.step("Открываем главную страницу"):
            page.open_main_page()

        with allure.step(f"Нажимаем на вопрос с индексом {index}"):
            page.click_question(index)

        with allure.step("Проверяем, что ответ не пустой"):
            answer = page.get_answer_text(index)
            assert answer.strip() != "", f"Ответ на вопрос {index} пустой"

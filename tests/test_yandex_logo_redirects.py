import pytest
import allure
from pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestYandexLogo:

    @allure.title("Проверка открытия главной страницы Дзена при клике на логотип Яндекса")
    @allure.description("""
    Проверка, что при клике на логотип Яндекса в новом окне открывается главная страница Дзена:
    1. Открыть главную страницу Самоката.
    2. Кликнуть по логотипу Яндекса.
    3. Дождаться открытия нового окна.
    4. Переключиться в новое окно.
    5. Проверить, что URL содержит 'dzen.ru'.
    """)
    def test_yandex_logo_opens_dzen_in_new_tab(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()

        with allure.step("Кликнуть на логотип Яндекса"):
            main_page.click_yandex_logo()

        with allure.step("Дождаться открытия второго окна"):
            main_page.wait_for_number_of_windows(2)

        with allure.step("Переключиться в новое окно"):
            main_page.switch_to_window(1)

        with allure.step("Дождаться, что URL содержит 'dzen.ru'"):
            main_page.wait_for_url_contains("dzen.ru")

        with allure.step("Проверить URL"):
            assert "dzen.ru" in driver.current_url

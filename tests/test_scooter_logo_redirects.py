import pytest
import allure
from pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestScooterLogoRedirect:

    @allure.title("Проверка редиректа по клику на логотип Самоката")
    @allure.description("""
    Проверка, что при клике на логотип Самоката происходит переход на главную страницу:
    1. Открыть главную страницу Самоката.
    2. Кликнуть по логотипу Самоката.
    3. Дождаться изменения URL.
    4. Проверить, что текущий URL соответствует главной странице.
    """)
    def test_click_scooter_logo_redirects_to_main_page(self, driver):
        page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            page.open_main_page()

        with allure.step("Кликнуть на логотип Самоката"):
            page.click_scooter_logo()

        with allure.step("Дождаться перехода на главную страницу"):
            page.wait_for_url_to_match("https://qa-scooter.praktikum-services.ru/")

        with allure.step("Проверить текущий URL"):
            assert page.get_current_url() == "https://qa-scooter.praktikum-services.ru/"

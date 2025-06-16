import pytest
import allure
from pages.locators import OrderPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.order_data import order_test_data


@allure.epic("UI-тесты")
@allure.feature("Оформление заказа самоката")
class TestOrderFromTopButton:

    @allure.title("Позитивный тест заказа самоката через верхнюю кнопку")
    @allure.description("""
    Проверка полного флоу заказа самоката:
    1. Переход на главную страницу.
    2. Нажатие на верхнюю кнопку 'Заказать'.
    3. Заполнение формы.
    4. Подтверждение заказа.
    5. Проверка появления модального окна с успешным заказом.
    """)
    @pytest.mark.parametrize("data", order_test_data)
    def test_order_from_top_button(self, driver, data):
        main_page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()

        with allure.step("Нажать верхнюю кнопку 'Заказать'"):
            main_page.click_order_button(top=True)

        order_page = OrderPage(driver)

        with allure.step("Заполнить форму заказа"):
            order_page.fill_order_form(data)

        with allure.step("Подтвердить заказ"):
            order_page.confirm_order()

        with allure.step("Проверить, что появилось окно успешного заказа"):
            order_page.assert_order_success_popup_visible()

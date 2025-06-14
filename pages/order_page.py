from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import OrderPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import MainPageLocators
import allure

class OrderPage(BasePage):

    def input_text(self, locator, text):
        field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        field.clear()
        field.send_keys(text)
    
    def fill_order_form(self, data):
        self.input_text(OrderPageLocators.NAME_FIELD, data["name"])
        self.input_text(OrderPageLocators.SURNAME_FIELD, data["surname"])
        self.input_text(OrderPageLocators.ADDRESS_FIELD, data["address"])
        self.select_metro_station(data["metro"])
        self.input_text(OrderPageLocators.PHONE_FIELD, data["phone"])
        self.click(OrderPageLocators.NEXT_BUTTON)

        self.driver.find_element(*OrderPageLocators.DATE_FIELD).click()
        day = data["date"].split(".")[0].lstrip("0")
        self.wait_for_clickable_and_click(OrderPageLocators.CALENDAR_DAY(day))
        
        self.select_rental_period(data["rental_period"])
        self.select_color(data["color"])
        self.input_text(OrderPageLocators.COMMENT_FIELD, data["comment"])
        self.click(OrderPageLocators.ORDER_BUTTON)


    def confirm_order(self):
        self.click(OrderPageLocators.YES_BUTTON)

    def order_success_popup_is_visible(self):
        return self.is_visible(OrderPageLocators.ORDER_CONFIRMED_POPUP)

    def select_metro_station(self, station_name):
        self.click(OrderPageLocators.METRO_FIELD)
        self.input_text(OrderPageLocators.METRO_FIELD, station_name)
        self.click(OrderPageLocators.METRO_DROPDOWN_OPTION)

    def select_rental_period(self, period):
        self.click(OrderPageLocators.RENTAL_DROPDOWN)
        self.click(OrderPageLocators.get_rental_period_option(period))

    def select_color(self, color):
        color = color.lower()
        if "чёрный" in color or "черный" in color:
            self.driver.find_element(*OrderPageLocators.COLOR_BLACK).click()
        if "серый" in color:
            self.driver.find_element(*OrderPageLocators.COLOR_GREY).click()

    def assert_element_visible(self, locator, name="element"):
        try:
            self.wait_for_visible(locator)
        except Exception:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name=f"{name}_not_visible",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Элемент '{name}' не отображается на странице")
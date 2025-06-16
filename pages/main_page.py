from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    URL = "https://qa-scooter.praktikum-services.ru/"

    def open_main_page(self):
        self.open(self.URL)
        self.close_cookie_banner()

    def click_question(self, index):
        locator = MainPageLocators.FAQ_QUESTION(index)
        self.scroll_to_element(locator)
        self.wait_for_clickable_and_click(locator)

    def get_answer_text(self, index):
        locator = MainPageLocators.FAQ_ANSWER(index)
        self.wait_for_clickable_and_click(locator)
        return self.driver.find_element(*locator).text
    
    def scroll_to_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def click_top_order_button(self):
        self.click(MainPageLocators.TOP_ORDER_BUTTON)

    def click_bottom_order_button(self):
        self.click(MainPageLocators.BOTTOM_ORDER_BUTTON)

    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)

    def close_cookie_banner(self):
        self.wait_for_clickable_and_click(MainPageLocators.COOKIE_BUTTON)

    def wait_for_number_of_windows(self, num):
        self.wait.until(EC.number_of_windows_to_be(num))

    def wait_for_url_contains(self, text):
        self.wait.until(EC.url_contains(text))

    def switch_to_window(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])

    def click_order_button(self, top=True):
        if top:
            self.click(MainPageLocators.TOP_ORDER_BUTTON)
        else:
            self.scroll_to_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
            self.click(MainPageLocators.BOTTOM_ORDER_BUTTON)

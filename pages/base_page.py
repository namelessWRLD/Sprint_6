import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        field = self.wait.until(EC.visibility_of_element_located(locator))
        field.clear()
        field.send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_element_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False
    
    def is_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False
        
    def wait_for_clickable_and_click(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()

    def wait_for_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def get_text_when_visible(self, locator, timeout=5):
        element = self.wait_for_visible(locator, timeout)
        return element.text    
    
    def assert_element_visible(self, locator, name="element"):
        try:
            element = self.wait_for_visible(locator)
            assert element.is_displayed()
        except Exception:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name=f"{name}_not_visible",
                attachment_type=allure.attachment_type.PNG
            )
            raise

    def wait_for_url_to_match(self, url, timeout=5):
        WebDriverWait(self.driver, timeout).until(EC.url_matches(url))

    def get_current_url(self):
        return self.driver.current_url                
    
    def wait_for_number_of_windows(self, num):
        self.wait.until(EC.number_of_windows_to_be(num))

    def wait_for_url_contains(self, text):
        self.wait.until(EC.url_contains(text))

    def switch_to_window(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])

    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)


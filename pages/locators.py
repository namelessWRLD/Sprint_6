from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопки "Заказать"
    TOP_ORDER_BUTTON = (By.XPATH, '//button[text()="Заказать"]')
    BOTTOM_ORDER_BUTTON = (By.XPATH, '(//button[text()="Заказать"])[2]')
    FAQ_QUESTION = lambda index: (By.ID, f"accordion__heading-{index}")
    FAQ_ANSWER = lambda index: (By.ID, f"accordion__panel-{index}")

    # FAQ: Вопрос и ответ по индексу
    @staticmethod
    def question_by_index(index):
        return (By.XPATH, f'(//div[contains(@id,"accordion__heading")])[{index}]')

    @staticmethod
    def answer_by_index(index):
        return (By.XPATH, f'(//div[contains(@id,"accordion__panel")])[{index}]')

    # Логотипы
    SCOOTER_LOGO = (By.XPATH, '//img[contains(@src, "scooter.png")]')
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    # Кнопка "Принять куки"
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")


class OrderPageLocators:
    #Личные данные
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_DROPDOWN_OPTION = (By.XPATH, "//div[@class='select-search__select']/ul/li")  # берём первый из списка
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    #Данные о заказе
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    CALENDAR_DAY = lambda day: (By.XPATH, f"//div[contains(@class, 'react-datepicker__day') and text()='{day}']")
    RENTAL_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[2]")

    def get_rental_period_option(period_text):
        return (By.XPATH, f"//div[@class='Dropdown-menu']/div[text()='{period_text}']")

    #Подтверждение заказа
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")

    #Успешное подтверждение
    ORDER_CONFIRMED_POPUP = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and contains(text(), 'Заказ оформлен')]")

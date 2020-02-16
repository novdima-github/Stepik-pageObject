from pages.base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math
import time


class ProductPage(BasePage):
    """Class ProductPage"""

    def add_to_cart(self):
        self.click_add_to_cart()
        self.solve_quiz_and_get_code()
        self.check_book_name()
        self.check_price()

    def click_add_to_cart(self):
        add_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_btn.click()
        time.sleep(1)

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME) \
            .text
        assert book_name == "Coders at Work", "Wrong book name"

    def check_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE) \
            .text
        assert price == "£19.99", "Wrong price"

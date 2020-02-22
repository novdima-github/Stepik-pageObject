"""Main page"""
from .base_page import BasePage
from .locators import MainPageLocators
import time


class MainPage(BasePage):
    """Class MainPage inherited from the superclass BasePage"""

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def check_that_book_is_absent(self):
        pass

    def add_to_cart(self):
        add_btn = self.browser.find_element(*MainPageLocators.ADD_TO_BASKET)
        add_btn.click()
        time.sleep(1)

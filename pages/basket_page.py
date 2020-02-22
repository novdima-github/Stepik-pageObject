from pages.base_page import BasePage
from .locators import BasketPageLocators


# from selenium.common.exceptions import NoAlertPresentException
# import math


class BasketPage(BasePage):
    """Class BasketPage"""

    def check_that_book_is_absent(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BOOK_NAME), \
            "Book is presented, but should not be"

    def check_that_checkout_button_is_absent(self):
        assert self.is_not_element_present(
            *BasketPageLocators.CHECKOUT), \
            "Book is presented, but should not be"

    def check_basket_word(self):
        basket = self.browser.find_element(*BasketPageLocators.BASKET_WORD).text
        print(basket)
        assert basket == "Basket", "Wrong text!"

    def check_text_basket_is_empty(self):
        basket_text = self.browser.find_element(
            *BasketPageLocators.BASKET_EMPTY_WORD).text
        print(basket_text)
        assert basket_text == "Your basket is empty. Continue shopping", \
            "Wrong text! "

from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.XPATH, '//a[contains(text(), "View basket")]')


class BasketPageLocators:
    BOOK_NAME = (By.XPATH, '//h1[contains(text(), "Coders at Work")]')
    BASKET_WORD = (By.XPATH, '//h1[contains(text(), "Basket")]')
    BASKET_EMPTY_WORD = (By.XPATH, '//p[contains(text(), "Your basket is '
                                   'empty")]')
    CHECKOUT = (By.XPATH, '//p[contains(text(), "Proceed to checkout")]')


class MainPageLocators:
    REGISTRATION_LINK = (By.CSS_SELECTOR, "#registration_link")
    ADD_TO_BASKET = (By.CSS_SELECTOR, "li:first-child button")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    """Locators for Product page"""
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe"
                                        ".alert-noicon.alert-success.fade.in "
                                        "> div")
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button[value='Add to basket']")
    BOOK_NAME = (By.XPATH, '//h1[contains(text(), "Coders at Work")]')
    PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")

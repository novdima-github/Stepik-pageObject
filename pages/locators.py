from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    REGISTRATION_LINK = (By.CSS_SELECTOR, "#registration_link")


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


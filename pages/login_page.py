from pages.base_page import BasePage
from pages.locators import LoginPageLocators
import time


class LoginPage(BasePage):
    """Class login page"""

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, "Wrong Login URL"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email1 = self.browser.find_element(*LoginPageLocators.EMAIL)
        email1.send_keys(email)
        password1 = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password1.send_keys(password)
        conf_password = self.browser.find_element(
            *LoginPageLocators.CONFIRM_PASSWORD)
        conf_password.send_keys(password)
        register = self.browser.find_element(*LoginPageLocators.REGISTER)
        time.sleep(1)  # Only to be able to see the results fulfilling
        register.click()
        time.sleep(2)  # Only to be able to see the results fulfilling

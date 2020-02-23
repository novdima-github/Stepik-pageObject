"""Run: pytest -v --tb=line --language=en test_main_page.py"""
# -*- coding: utf-8 -*-
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest
import time

MAINPAGE_LINK = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, MAINPAGE_LINK)  # инициализируем Page Object,
    #  передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, MAINPAGE_LINK)
    page.open()
    # page.add_to_cart() # Uncomment to fail the test (Add product to basket)
    page.go_to_basket()
    time.sleep(1)
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_that_book_is_absent()
    basket_page.check_that_checkout_button_is_absent()
    basket_page.check_basket_word()
    basket_page.check_text_basket_is_empty()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, MAINPAGE_LINK)
    page.open()
    page.should_be_login_link()


@pytest.mark.login_guest
class TestLoginFromMainPage:
    """Test Class"""
    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, MAINPAGE_LINK)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, MAINPAGE_LINK)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
# -*- coding: utf-8 -*-

import pytest
import time
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage


@pytest.mark.need_review
@pytest.mark.parametrize('promo_offer', ["0", "1", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at" \
           f"-work_207/?promo=offer{promo_offer}"
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_to_cart()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at" \
           "-work_207/"
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_to_cart()
    product_page.message_should_not_be_appeared()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at" \
           "-work_207/"
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.message_should_not_be_appeared()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at" \
           "-work_207/"
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_to_cart()
    product_page.message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the" \
           "-city-and-the-stars_95/ "
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the" \
           "-city-and-the-stars_95/ "
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-age-of" \
           "-the-pussyfoot_89/ "
    page = ProductPage(browser, link)
    page.open()
    # page.add_to_cart() # Uncomment to fail the test (Add product to basket)
    page.go_to_basket()
    time.sleep(1)
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_that_book_is_absent()
    basket_page.check_that_checkout_button_is_absent()
    basket_page.check_basket_word()
    basket_page.check_text_basket_is_empty()


@pytest.mark.registered_user
class TestUserAddToBasketFromProductPage:
    """Test Users"""
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        page.register_new_user(email, '123123abc!')
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at" \
               "-work_207/"
        page = MainPage(browser, link)
        page.open()
        product_page = ProductPage(browser, browser.current_url)
        product_page.message_should_not_be_appeared()

    @pytest.mark.need_review    
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at" \
               "-work_207/?promo=newYear2019 "
        page = MainPage(browser, link)
        page.open()
        product_page = ProductPage(browser, browser.current_url)
        product_page.add_to_cart()

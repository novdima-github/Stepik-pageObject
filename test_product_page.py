"""Run: pytest -v --tb=line --language=en test_main_page.py"""
# -*- coding: utf-8 -*-
import pytest

from pages.main_page import MainPage
from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в
    # конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_to_cart()

@pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket1(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at" \
           f"-work_207/?promo=offer{promo_offer}"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в
    # конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_to_cart()
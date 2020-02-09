import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/"

def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector("#login_link")
    time.sleep(1)
    login_link.click()

def test_guest_can_go_to_login_page(browser):
   browser.get(link)
   go_to_login_page(browser)

# def test_add_to_cart_button_exist(browser):
#     browser.get(link)
#     time.sleep(5)
#     add_to_cart_button = WebDriverWait(browser, 5).\
#         until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn-add-to-basket')))
#     assert add_to_cart_button, "No 'Add to basket button exist'..."
#

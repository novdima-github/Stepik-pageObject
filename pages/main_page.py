"""Main page"""
from .base_page import BasePage


class MainPage(BasePage):
    """Class MainPage inherited from the superclass BasePage"""
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

class BasePage:
    """Super class"""
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        """Open browser with URL"""
        self.browser.get(self.url)
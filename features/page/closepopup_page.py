from selenium.webdriver.common.by import By

class Closepopup_Page:
    URL = 'https://jules.app/search/all'

    def __init__(self, browser):
        self.driver = browser.driver

    def get_page(self):
        self.driver.get(self.URL)

    #def popup_is_visible(self):


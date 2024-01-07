from time import sleep

from selenium.webdriver.common.by import By


class Logout_Page:
    LOGOUT_URL = 'https://jules.app/'
    ACCOUNT_BUTTON_SELECTOR = (By.CSS_SELECTOR, 'svg[data-test-id="user-options-business-button"]')
    LOGOUT_BUTTON_SELECTOR = (By.CSS_SELECTOR, 'ul[data-test-id="logout-option-business"]')

    def __init__(self, browser):
        self.driver = browser.driver

    def get_logout_page(self):
        self.driver.get(self.LOGOUT_URL)

    def click_account_button(self):
        account_button = self.driver.find_element(*self.ACCOUNT_BUTTON_SELECTOR)
        account_button.click

        sleep(15)

    def click_logout_button(self):
        logout_button = self.driver.find_element(*self.LOGOUT_BUTTON_SELECTOR)
        logout_button.click

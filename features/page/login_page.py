from selenium.webdriver.common.by import By
from time import sleep

class Login_Page:
    URL = 'http://jules.app/'
    USERNAME_SELECTOR = (By.CSS_SELECTOR, 'input[placeholder="Enter your email"]')
    PASSWORD_SELECTOR = (By.CSS_SELECTOR, 'input[placeholder="Enter your password"]')
    LOGIN_BUTTON_SELECTOR = (By.CSS_SELECTOR, 'button[data-test-id="login-button"]')
    POPUP_CANCEL_BUTTON = (By.CSS_SELECTOR, 'button[id="onesignal-slidedown-cancel-button"]')


    def __init__(self, browser):
        self.driver = browser.driver

    def get_page(self):
        self.driver.get(self.URL)

    def input_username(self, username):
        username_input = self.driver.find_element(*self.USERNAME_SELECTOR)
        username_input.send_keys(username)

    def input_password(self, password):
        password_input = self.driver.find_element(*self.PASSWORD_SELECTOR)
        password_input.send_keys(password)


    def click_login_button(self):
        login_button = self.driver.find_element(*self.LOGIN_BUTTON_SELECTOR)
        login_button.click()
        sleep(5)


    def get_url(self):
        return self.driver.current_url


    def click_cancel_button(self):
        cancel_button = self.driver.find_element(*self.POPUP_CANCEL_BUTTON)
        check_cancel_button = cancel_button.is_displayed()
        if check_cancel_button is True:
            cancel_button.click()
        sleep(5)

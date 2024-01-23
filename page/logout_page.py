from selenium.webdriver.common.by import By


class Logout_Page:
    URL = 'https://jules.app/search/all'
    ACCOUNT_BUTTON_SELECTOR = (By.CSS_SELECTOR, 'svg[data-test-id="user-options-business-button"]')
    LOGOUT_BUTTON_SELECTOR = (By.CSS_SELECTOR, 'div[data-test-id="logout-option-business"]')
    CONFIRM_LOGOUT_SELECTOR = (By.CSS_SELECTOR, 'button[data-test-id="confirm-logout-button"]')


    def __init__(self, browser):
        self.driver = browser.driver

    def get_page(self):
        self.driver.get(self.URL)

    def click_account_button(self):
        account_button = self.driver.find_element(*self.ACCOUNT_BUTTON_SELECTOR)
        account_button.click()

    def click_logout_button(self):
        logout_button = self.driver.find_element(*self.LOGOUT_BUTTON_SELECTOR)
        logout_button.click()

    def click_confirm_logout(self):
        confirm_logout = self.driver.find_element(*self.CONFIRM_LOGOUT_SELECTOR)
        confirm_logout.click()


    def get_url(self):
        return self.driver.current_url

# from time import sleep
#
# from selenium.webdriver.common.by import By
#
#
# class Closepopup_Page:
#     URL = 'https://jules.app/search/all'
#     POPUP_CANCEL_BUTTON = (By.CSS_SELECTOR, 'button[id="onesignal-slidedown-cancel-button"]')
#
#     def __init__(self, browser):
#         self.driver = browser.driver
#
#     def get_page(self):
#         self.driver.get(self.URL)
#
#     def click_cancel_button(self):
#         sleep(5)
#         cancel_button = self.driver.find_element(*self.POPUP_CANCEL_BUTTON)
#         check_cancel_button = self.driver.find_element(*self.POPUP_CANCEL_BUTTON).is_displayed()
#         if check_cancel_button is True:
#             cancel_button.click()
#         sleep(5)

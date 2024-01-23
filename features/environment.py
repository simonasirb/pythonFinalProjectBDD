from features.browser import Browser
from page.login_page import Login_Page
from page.logout_page import Logout_Page


def before_all(context):
    context.browser = Browser()
    context.login_page = Login_Page(context.browser)
    context.logout_page = Logout_Page(context.browser)


def after_all(context):
    context.browser.quit()

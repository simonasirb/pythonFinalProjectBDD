from features.browser import Browser
from features.page.login_page import Login_Page
from features.page.logout_page import Logout_Page
#from features.page.closepopup_page import Closepopup_Page


def before_all(context):
    context.browser = Browser()
    context.login_page = Login_Page(context.browser)
#    context.closepopup_page = Closepopup_Page(context.browser)
    context.logout_page = Logout_Page(context.browser)


def after_all(context):
    context.browser.quit()

from behave import *


@Given('I am on the main page')
def step_impl(context):
    context.logout_page.get_logout_page()


@When('I click on account button')
def step_impl(context):
    context.logout_page.click_account_button()


@When('I click on logout button')
def step_impl(context):
    context.logout_page.click_logout_button()


# @Given('I am on the login page')
# def step_impl(context):
#     context.login_page.get_page()


# @When('I input a valid username')
# def step_impl(context):
#     context.login_page.input_username('simonasirb@outlook.com')
#
#
# @When('I input a valid password')
# def step_impl(context):
#     context.login_page.input_password('FPTest1!')
#
#
# @When('I click on login button')
# def step_impl(context):
#     context.login_page.click_login_button()

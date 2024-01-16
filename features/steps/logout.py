from behave import *


@Given('I am on the main page')
def step_impl(context):
    context.logout_page.get_page()


@When('I click on account button')
def step_impl(context):
    context.logout_page.click_account_button()


@When('I click on logout button')
def step_impl(context):
    context.logout_page.click_logout_button()

@When ('I confirm logout')
def step_impl(context):
    context.logout_page.click_confirm_logout()

@Then ('I am on the login page')
def step_impl(context):
    assert context.logout_page.get_url() == 'https://jules.app/sign-in'





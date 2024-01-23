from behave import *

@Given('I am on the main page')
def step_impl(context):
    assert context.closepopup_page.get_page()

@When('The popup is visible')
def step_impl(context):
    pass

@Then('I click on cancel button')
def step_impl(context):
    pass

from behave import *

@Given('I am on the home page')
def step_impl(context):
    #assert context.closepopup_page.get_page()
    pass

@When('I click the cancel button')
def step_impl(context):
    #context.closepopup_page.click_cancel_button()
    pass

@Then('The popup is not visible')
def step_impl(context):
    pass

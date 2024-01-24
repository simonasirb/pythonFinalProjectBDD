from behave import *


@Given('I am on the login page')
def step_impl(context):
    context.login_page.get_page()


@When('I input a valid username')
def step_impl(context):
    context.login_page.input_username('simonasirb@outlook.com')


@When('I input an invalid password')
def step_impl(context):
    context.login_page.input_password('FPTest231')


@Then('I am still on the login page')
def step_impl(context):
    assert context.login_page.get_url() == 'https://jules.app/sign-in'


@When('I click on login button')
def step_impl(context):
    context.login_page.click_login_button()


@When('I input a invalid username')
def step_impl(context):
    context.login_page.input_username('simonadsasirb@outlook.com')


@When('I input a valid password')
def step_impl(context):
    context.login_page.input_password('FPTest1!')


@Then('I am on the main page')
def step_impl(context):
    assert context.login_page.get_url() == 'https://jules.app/search/all'


@Given('I am on the home page')
def step_impl(context):
    assert context.login_page.get_url() == 'https://jules.app/search/all'


@When('I click the cancel button')
def step_impl(context):
    context.login_page.click_cancel_button()


@Then('The popup is not visible')
def step_impl(context):
    pass


@Given('I am on the start page')
def step_impl(context):
    assert context.login_page.get_url() == 'https://jules.app/search/all'


@When('I click on add button from menu')
def step_impl(context):
    context.login_page.click_add_button()


@When('I click on person button')
def step_impl(context):
    context.login_page.click_person_button()


@When('I input first name')
def step_impl(context):
    context.login_page.input_first_name('Popescu')


@When('I click on save button')
def step_impl(context):
    context.login_page.click_save_button()


@Then('The person was added')
def step_impl(context):
    pass

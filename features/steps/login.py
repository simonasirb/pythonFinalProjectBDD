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


@Then('I click on finish button')
def step_impl(context):
    context.login_page.click_finish_button()


@When('I input last name')
def step_impl(context):
    context.login_page.input_last_name('Ion')


@When('I input again first name')
def step_impl(context):
    context.login_page.input_first_name('Ionescu')


@When('I input again last name')
def step_impl(context):
    context.login_page.input_last_name('George')


@Given('I am on the initial page')
def step_impl(context):
    assert context.login_page.get_url() == 'https://jules.app/search/all'


@When('I click the people button')
def step_impl(context):
    context.login_page.click_people_button()


@Then('I see the list of people')
def step_impl(context):
    assert context.login_page.get_url() == 'https://jules.app/people'


@Then('The I select the person to delete')
def step_impl(context):
    context.login_page.click_select_button()


@Then('I click on delete button')
def step_impl(context):
    context.login_page.click_delete_button()


@Then('I confirm delete person')
def step_impl(context):
    context.login_page.click_confirm_delete_button()

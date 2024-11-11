from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
@given('Open reelly page')
def open_reelly(context):
    context.app.login_page.open_reelly()
    context.driver.implicitly_wait(5)
@when('Enter email and password')
def input_email_and_password(context):
    context.app.login_page.input_email_and_password()
@when('Click on Continue button')
def click_continue_btn(context):
    context.app.login_page.click_continue_btn()
@when('Click on settings option')
def click_on_market(context):
    context.app.main_page.open_main()
@then('verify user be able to see three options that available')
def verify_three_options_available(context):
    context.app.base_page.verify_three_options_available()
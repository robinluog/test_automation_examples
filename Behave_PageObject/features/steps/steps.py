from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import *


@given ('I\'m on {page} page')
def open_page(context, page):
    context.page = eval('{}Page'.format(page))(context)

@when  ('I click {some}')
def click_some(context, some):
    context.page.click_(some)

@then  ('I see message: {}')
def see_some(context, text):
    context.page.see_text(text)

@step ('I fill form')
def fill_form(context):
    for row in context.table:
        field = row['name']
        value = row['value']
        context.page.fill_signup_form(field, value)

@then  ('{} page displayed')
def check_page(context, name):
    context.page.check_current_page(name)

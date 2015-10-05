from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('I\'m on "{page}" page')
def open_page(context, page):
    context.map = context.mapping[page]
    context.browser.maximize_window()
    context.browser.get(context.map['url'])

@step('I click on "{item}"')
def click_button(context, item):
    element = WebDriverWait(context.browser, 2).until(EC.presence_of_element_located((By.XPATH, context.map[item])))
    element.click()

@step('I see "{text}"')
def chek_what_i_see(context, text):
    try:
        WebDriverWait(context.browser, 2).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(),"'+text+'")]')))
    except:
        WebDriverWait(context.browser, 2).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'"+text+"')]")))

@when('I fill form')
def fill_form(context):
    for row in context.table:
        input_ = context.map[row['name']]
        value_ = context.map[row['value']]
        element = WebDriverWait(context.browser, 2).until(EC.presence_of_element_located((By.XPATH, input_)))
        element.send_keys(value_)

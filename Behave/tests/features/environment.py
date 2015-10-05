from mapping import site_mapping
from selenium import webdriver


def before_all(context):
    context.browser = webdriver.Firefox()
    context.mapping = site_mapping


def after_all(context):
    context.browser.close()

from lettuce import before, after, world
from mapping import site_mapping
from selenium import webdriver


@before.all
def setup():
    world.browser = webdriver.Firefox()
    world.mapping = site_mapping


@after.all
def tear_down(total):
    world.browser.close()

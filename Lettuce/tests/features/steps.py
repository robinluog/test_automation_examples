from lettuce import step, world
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@step('I go to "(.*)" page')
def open_page(step, page):
    world.map = world.mapping[page]
    world.browser.maximize_window()
    world.browser.get(world.map['url'])

@step('I click on "(.*)" in "(.*)"')
def click_button(step, item, page):
    world.map = world.mapping[page]
    element = WebDriverWait(world.browser, 10).until(EC.presence_of_element_located((By.XPATH, world.map[item])))
    element.click()

@step('I see "(.*)" in "(.*)"')
def chek_what_i_see(step, item, page):
    world.map = world.mapping[page]
    WebDriverWait(world.browser, 12).until(EC.presence_of_element_located((By.XPATH, world.map[item])))

@step('I fill "(.*)" by "(.*)" in "(.*)"')
def fill_field(step, item, value, page):
    world.map = world.mapping[page]
    value = world.map[value]
    element = WebDriverWait(world.browser, 10).until(EC.presence_of_element_located((By.XPATH, world.map[item])))
    element.send_keys(value)

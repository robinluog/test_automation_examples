from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators as loc


class BasePage(object):
    def __init__(self, context):
        self.context = context
        global browser
        browser = self.context.browser

    def click_element(self, el):
        element = WebDriverWait(browser, 2).until(EC.presence_of_element_located(el))
        element.click()

    def see_text(self, text):
        try:
            element = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(),"{}")]'.format(text))))
        except:
            try:
                element = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'{}')]".format(text))))
            except:
                text = text.encode('utf-8', 'ignore')
                element = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(),"{}")]'.format(text))))

    def fill_form(self, locator, field, value):
        element = WebDriverWait(browser, 2).until(EC.presence_of_element_located(getattr(locator, field)))
        element.send_keys(getattr(locator, value))

    def check_current_page(self, name):
        assert browser.current_url == getattr(loc.Pages, name)


class SignUpPage(BasePage):
    def __init__(self, context):
        self.driver = context
        self.page = BasePage(self.driver)
        browser.get(loc.SignUpLocators.URL)

    def click_(self, el):
        self.page.click_element(getattr(loc.SignUpLocators, el))

    def fill_signup_form(self, field, value):
        self.page.fill_form(loc.SignUpLocators, field, value)

class MainPage(BasePage):
    def __init__(self, context):
        self.driver = context
        self.page = BasePage(self.driver)
        browser.get(loc.MainPageLocators.URL)

    def click_(self, el):
        self.page.click_element(getattr(loc.MainPageLocators, el))

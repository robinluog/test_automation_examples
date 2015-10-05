from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import locators


class BasePage(object):

    def __init__(self):
        self.browser = webdriver.Firefox()
        self.map = locators

    def click_element(self, button):
        element = WebDriverWait(self.browser, 2).until(EC.presence_of_element_located(button))
        element.click()

    def go2(self, url):
        self.browser.get(url)



class SignUpPage(BasePage):

    def openPage(self):
        BasePage.go2(self, "https://my-release.solidopinion.com/signup")

    def signup(self):
        BasePage.click_element(self, self.map.SignUpLocators.SIGNUP_BUTTON)


# a = SignUpPage()
# a.openPage()
# a.signup()
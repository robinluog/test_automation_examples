from selenium.webdriver.common.by import By
import time
from base_page import BasePage

class SignUpPage(BasePage):
    PAGE = "SIGNUP"
    FB_BUTTON = (By.XPATH, "//a[contains(text(),'F')]")
    TW_BUTTON = (By.XPATH, "//a[contains(text(),'T')]")
    VK_BUTTON = (By.XPATH, "//a[contains(text(),'V')]")
    GG_BUTTON = (By.XPATH, "//a[contains(text(),'G')]")
    YH_BUTTON = (By.XPATH, "//a[contains(text(),'Y')]")
    NAME_INPUT = (By.XPATH, "//input[@id='name']")
    NAME = "Some Name"
    EMAIL_INPUT = (By.XPATH, "//input[@id='email']")
    EMAIL = "some_mail+{}@gmail.com".format(time.time())
    EMAIL_BAD = "some_mail@gmailcom"
    PASS_INPUT = (By.XPATH, "//input[@id='password']")
    PASS2_INPUT = (By.XPATH, "//input[@id='password2']")
    PASS_BAD = "1",
    PASSWORD = "123456789012345678901234567890"
    SIGNUP_BUTTON = (By.XPATH, "//button[@id='go_signup']")
    TERMS_LINK = (By.XPATH, "//form[contains(concat('',@class,''),'form-signin')]//a[contains(text(),'Terms and Policies')]")
    HAVE_ACCOUNT_LINK = (By.XPATH, "//div[@id='conteiner-signin']//a[contains(text(),'Already have an account?')]")
    CLOSE_ALERT_MSG = (By.XPATH, "//button[@class='close']")

    def __init__(self, context):
        super(SignUpPage, self).__init__(context)
        self.open_page(self.PAGE)

    def click_(self, el):
        self.click_element(eval('self.{}'.format(el)))

    def fill_signup_form(self, field, value):
        self.fill_form(eval('self.{}'.format(field)), eval('self.{}'.format(value)))


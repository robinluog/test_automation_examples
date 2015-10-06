from selenium.webdriver.common.by import By
import time


class Pages(object):
    DISCUSSION = "http://solidopinion.com/soliddiscussion/"

class SignUpLocators(object):
    URL = "https://my-release.solidopinion.com/signup"
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

class MainPageLocators(object):
    URL = "http://solidopinion.com"
    DISCUSSION_BUTTON = (By.XPATH, "//a[contains(text(),'SolidDiscussion')]")

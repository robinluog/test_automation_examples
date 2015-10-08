from selenium.webdriver.common.by import By
from base_page import BasePage


class MainPage(BasePage):
    PAGE = "MAIN"
    DISCUSSION_BUTTON = (By.XPATH, "//a[contains(text(),'SolidDiscussion')]")

    def __init__(self, context):
        super(MainPage, self).__init__(context)
        self.open_page(self.PAGE)

    def click_(self, el):
        self.click_element(eval('self.{}'.format(el)))

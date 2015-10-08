from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    MAIN = "http://solidopinion.com"
    DISCUSSION = "http://solidopinion.com/soliddiscussion/"
    SIGNUP = "https://my-release.solidopinion.com/signup"

    def __init__(self, context):
        self.context = context
        self.browser = self.context.browser

    def open_page(self, page_name):
        self.browser.get(eval('self.{}'.format(page_name)))

    def click_element(self, el):
        element = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(el))
        element.click()

    def see_text(self, text):
        try:
            WebDriverWait(self.browser, 2).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(),"{}")]'.format(text))))
        except:
            try:
                WebDriverWait(self.browser, 2).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'{}')]".format(text))))
            except:
                text = text.encode('utf-8', 'ignore')
                WebDriverWait(self.browser, 2).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(),"{}")]'.format(text))))

    def fill_form(self, field, value):
        element = WebDriverWait(self.browser, 2).until(EC.presence_of_element_located(field))
        element.send_keys(value)

    def check_current_page(self, name):
        assert self.browser.current_url == eval('self.{}'.format(name))

from baidu_search.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time

class SearchPage(BasePage):
    url="https://baidu.com"
    search_input = (By.CSS_SELECTOR, "#kw")
    search_button = (By.CSS_SELECTOR, "#su")

    def load(self):
        self.access(self.url)

    def search(self, phrase):
        self.find_element(self.search_input).clear()
        self.find_element(self.search_input).send_keys(phrase)
        self.find_element(self.search_button).click()
        time.sleep(5)

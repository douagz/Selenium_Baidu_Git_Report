from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ResultPage(BasePage):
    search_input = (By.CSS_SELECTOR, "#kw")
    result_links = (By.CSS_SELECTOR, "h3.c-title>a")

    def result_link_titles(self):
        elements = self.find_elements(self.result_links)
        titles = []
        for e in elements:
            titles.append(e.text)
        return titles

    def result_link_titles_contain_phrase(self, phrase):
        titles = self.result_link_titles()
        match_titles = [m for m in titles if phrase.lower() in m.lower()]
        return len(match_titles) > 0



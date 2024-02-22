from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,os
from selenium.webdriver.common.by import By

class BasePage:

    def __init__(self,driver):
        self.driver=driver

    def access(self,url):
        self.driver.get(url)
        time.sleep(5)

    def get_title(self):
        return self.driver.title

    def is_element_visible(self, locator):
        for i in range(3):
            try:
                element=WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(locator))
                return element
            except TimeoutError:
                print(f"{i} time, {locator} is not found")
                time.sleep(2)
        return False

    def find_element(self, locator):
        element=WebDriverWait(self.driver,30).until(EC.presence_of_element_located(locator))
        return element

    def find_elements(self, locator):
        elements=WebDriverWait(self.driver,30).until(EC.presence_of_all_elements_located(locator))
        return elements





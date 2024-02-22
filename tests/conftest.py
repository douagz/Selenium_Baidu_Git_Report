import pytest
from ..pages.search import SearchPage
from pages.result import ResultPage
from selenium import webdriver

driver=None

@pytest.fixture(scope="session",autouse=False)
def baidu_driver():
    global driver
    if driver is None:
        options = webdriver.ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--implicit=10')
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option('excludeSwitches', ['enable-automation'])

        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(30)
    return driver

@pytest.fixture(scope="session",autouse=False)
def baidu_search_page(baidu_driver):
    baidu_search_page=SearchPage(baidu_driver)
    return baidu_search_page

@pytest.fixture(scope="session",autouse=False)
def baidu_result_page(baidu_driver):
    baidu_result_page=ResultPage(baidu_driver)
    return baidu_result_page

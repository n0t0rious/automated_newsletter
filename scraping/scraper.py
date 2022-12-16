from scraping.locators import MainPageLocators
from selenium import webdriver
from scraping.constants import BASE_URL
from selenium.webdriver.chrome.options import Options


class Scraper:
    def __init__(self, teardown=False):
        self.teardown = teardown
        self.options = Options()
        self.options.add_argument("--incognito")
        self.options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.maximize_window()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.driver.quit()

    def land_first_page(self):
        self.driver.get(BASE_URL)

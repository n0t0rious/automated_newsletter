from packages.scraping.constants import BASE_URL
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


class BaseDriver:
    """Constructor for each webpage, takes a driver"""
    url = BASE_URL

    def __init__(self):
        self.options = Options()
        self.options.add_argument("--incognito")
        self.options.add_argument("start-maximized")
        self.options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.maximize_window()

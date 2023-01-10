from scraping.basedriver import BaseDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from scraping.element import PageElement


class Scraper(BaseDriver):
    def __init__(self, teardown=False):
        super().__init__()
        self.teardown = teardown

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.driver.quit()

    def land_first_page(self):
        self.driver.get(self.url)

    def land_page(self, url):
        self.driver.get(url)

    def select_category(self, *category):
        category = self.driver.find_element(*category)
        category.send_keys(Keys.RETURN)

    # TODO: Find a common element / way to print the links across each locator, currently code below only works for
    #       US_Markets 
    def get_stories(self):
        links = []

        collection = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//ul[contains(@class, 'story-collection__three_columns__2Th0B story-collection__list__2M49i')]")
        )).find_elements(By.TAG_NAME, 'li')

        for story in collection:
            href = story.find_element(By.TAG_NAME, 'a').get_attribute('href')
            links.append(href)

        print(links)
        print(len(collection))
    # TODO: Reformat code in a more logical and object oriented way



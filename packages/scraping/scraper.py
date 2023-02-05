import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from packages.scraping.basedriver import BaseDriver
from packages.scraping.constants import PARAGRAPH_LENGTH, LOGIN_URL
from packages.scraping.element import wait
from packages.scraping.locators import MainPageLocators as mP
from packages.scraping.login_handler import retrieve_credentials


class Scraper(BaseDriver):
    def __init__(self, teardown=False):
        super().__init__()
        self.teardown = teardown

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.driver.quit()

    def land_homepage(self):
        self.driver.get(self.url)

    def land_page(self, url: str):
        self.driver.get(url)

    def select_category(self, *category: tuple):
        wait(self.driver, category).send_keys(Keys.RETURN)

    def get_stories(self):
        collection = wait(self.driver, mP.COLLECTIONS).find_elements(By.TAG_NAME, 'li')
        links = tuple((story.find_element(*mP.STORIES).get_attribute('href') for story in collection))
        return links

    def get_content(self):
        contents = {}
        links = self.get_stories()
        for story_num, link in enumerate(links):
            self.land_page(link)
            paragraph = wait(self.driver, mP.ARTICLE).find_elements(By.TAG_NAME, 'p')
            paragraphs = [paragraph[paragraph_num].text for paragraph_num in range(PARAGRAPH_LENGTH)]
            contents[story_num] = {"".join(paragraphs): links[story_num]}
        return contents

    def login(self):
        self.land_page(LOGIN_URL)
        credentials = retrieve_credentials()

        email_input = wait(self.driver, mP.EMAIL_INPUT)
        _pass = wait(self.driver, mP.PASS_INPUT)

        time.sleep(1)

        email_input.send_keys(credentials[0])
        _pass.send_keys(credentials[1])
        _pass.submit()

        time.sleep(1)

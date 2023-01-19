import time

from scraping.basedriver import BaseDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scraping.locators import MainPageLocators as mP
from scraping.login_handler import retrieve_credentials
from scraping.element import wait


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

    def land_page(self, url: str):
        self.driver.get(url)

    def select_category(self, *category: tuple):
        wait(self.driver, category).send_keys(Keys.RETURN)

    def get_stories(self):
        links = []
        collection = wait(self.driver, mP.COLLECTIONS).find_elements(By.TAG_NAME, 'li')
        # TODO fix href locator to only pull relevant link
        for story in collection:
            href = story.find_element(By.TAG_NAME, 'a').get_attribute('href')
            links.append(href)
        return links

    def get_content(self):
        contents = {}
        links = self.get_stories()
        for story_num, link in enumerate(links):
            self.land_page(link)
            paragraph = wait(self.driver, mP.ARTICLE).find_elements(By.TAG_NAME, 'p')
            paragraphs = [paragraph[paragraph_num].text for paragraph_num in range(2)]
            contents[story_num] = "".join(paragraphs)
        print(contents[0])

    def login(self):
        sign_in = wait(self.driver, mP.SIGN_IN)
        sign_in.send_keys(Keys.RETURN)
        credentials = retrieve_credentials()
        # TODO: Potential issue with skipping over pass input and only sending email
        _pass = wait(self.driver, mP.PASS_INPUT)
        _pass.send_keys(credentials[0])

        email_input = wait(self.driver, mP.EMAIL_INPUT)
        email_input.send_keys(credentials[1])
        email_input.submit()

    # TODO  Find a way to extract headers alongside links and store them

    # TODO  Reformat get_content() & get_stories()  in a more logical and object oriented way, consider refactoring
    #       reused code into helper funcs in a new class

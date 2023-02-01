import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from scraping.basedriver import BaseDriver
from scraping.locators import MainPageLocators as mP
from scraping.login_handler import retrieve_credentials
from scraping.element import wait
from scraping.constants import PARAGRAPH_LENGTH


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

    # TODO fix href locator to only pull relevant link
    def get_stories(self):
        collection = wait(self.driver, mP.COLLECTIONS).find_elements(By.TAG_NAME, 'li')
        links = tuple((story.find_element(By.TAG_NAME, 'a').get_attribute('href') for story in collection))
        return links

    def get_content(self):
        # contents = {}
        # links = self.get_stories()
        # for story_num, link in enumerate(links):
        #     self.land_page(link)
        #     paragraph = wait(self.driver, mP.ARTICLE).find_elements(By.TAG_NAME, 'p')
        #     paragraphs = [paragraph[paragraph_num].text for paragraph_num in range(PARAGRAPH_LENGTH)]
        #     contents[story_num] = "".join(paragraphs)
        # return contents
        contents = {}
        links = self.get_stories()
        for story_num, link in enumerate(links):
            self.land_page(link)
            paragraph = wait(self.driver, mP.ARTICLE).find_elements(By.TAG_NAME, 'p')
            paragraphs = [paragraph[paragraph_num].text for paragraph_num in range(PARAGRAPH_LENGTH)]
            contents[story_num] = {"".join(paragraphs): links[story_num]}
        return contents

    def login(self):
        wait(self.driver, mP.SIGN_IN).send_keys(Keys.RETURN)
        credentials = retrieve_credentials()

        email_input = wait(self.driver, mP.EMAIL_INPUT)
        _pass = wait(self.driver, mP.PASS_INPUT)

        time.sleep(1)

        email_input.send_keys(credentials[0])
        _pass.send_keys(credentials[1])
        _pass.submit()

    # TODO: Find a way to extract links and output them alongside stories in pdf

    # TODO: Figure out the best way to distribute and run program from the command line

    # TODO: Consolidate PageElement class

    # TODO: Reformat get_content() & get_stories()  in a more logical and object oriented way, consider refactoring
    #       eused code into helper funcs in a new class

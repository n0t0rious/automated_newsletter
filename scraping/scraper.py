from scraping.basedriver import BaseDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        category = self.driver.find_element(*category)
        category.send_keys(Keys.RETURN)

    def get_stories(self):
        links = []

        collection = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//ul[contains(@class, 'story-collection__three_columns__2Th0B story-collection__list__2M49i')]")
        )).find_elements(By.TAG_NAME, 'li')

        for story in collection:
            href = story.find_element(By.TAG_NAME, 'a').get_attribute('href')
            links.append(href)

        return links
        # print(links)

    def get_content(self):
        contents = {}
        links = self.get_stories()
        for i, j in enumerate(links):
            self.land_page(j)
            paragraph = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'article-body__content__17Yit paywall-article')]")
            )).find_elements(By.TAG_NAME, 'p')
            print(len(paragraph))
            paragraphs = [paragraph[k].text for k in range(2)]
            contents[i] = "-".join(paragraphs)
        print(contents[0])
        print(len(contents))

        # Seems to be working, but I reached the "Article limit", will implement login logic and test again

    # TODO 1: Add login function and logic in an object oriented way & Figure out how to safely read in password and
    #         email for login

    # TODO 2: Test that method to extract paragraphs and store them works
    #         2.1 use dictionary to store individual stories, story num as key & values will be joined paragraphs

    # TODO: Reformat get_content() & get_stories()  in a more logical and object oriented way, consider refactoring
    #       reused code into helper funcs in a new class

from selenium.webdriver.common.by import By


class MainPageLocators:
    # Categories
    US_MARKETS = (By.XPATH, "//button[@data-id='/markets/us/']")
    EU_MARKETS = (By.XPATH, "//button[@data-id='/markets/europe/']")
    MACRO_MATTERs = (By.XPATH, "//button[@data-id='/markets/macromatters/']")
    STOCKS = (By.XPATH, "//button[@data-id='/markets/stocks/']")
    DEALS = (By.XPATH, "//button[@data-id='/markets/deals/']")

    # Stories
    COLLECTIONS = (By.XPATH, "//ul[contains(@class, 'story-collection__three_columns__2Th0B "
                             "story-collection__list__2M49i')]")
    ARTICLE = (By.XPATH, "//div[contains(@class, 'article-body__content__17Yit paywall-article')]")

    # Login
    SIGN_IN = (By.XPATH, '//a[@href="https://www.reuters.com/signin/?redirect=https%3A%2F%2Fwww.reuters.com%2Fmarkets'
                         '%2F"]')
    PASS_INPUT = (By.NAME, 'password')
    EMAIL_INPUT = (By.NAME, 'email')

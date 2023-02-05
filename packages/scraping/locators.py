from selenium.webdriver.common.by import By


class MainPageLocators:
    # Category locators
    US_MARKETS = (By.XPATH, "//button[@data-id='/markets/us/']")
    EU_MARKETS = (By.XPATH, "//button[@data-id='/markets/europe/']")
    MACRO_MATTERS = (By.XPATH, "//button[@data-id='/markets/macromatters/']")
    STOCKS = (By.XPATH, "//button[@data-id='/markets/stocks/']")
    DEALS = (By.XPATH, "//button[@data-id='/markets/deals/']")
    COMMODITIES = (By.XPATH, "//button[@data-id='/markets/commodities/']")

    # Content locators
    COLLECTIONS = (By.XPATH, "//ul[contains(@class, 'story-collection__three_columns__2Th0B "
                             "story-collection__list__2M49i')]")
    ARTICLE = (By.XPATH, "//div[contains(@class, 'article-body__content__17Yit paywall-article')]")
    STORIES = (By.CSS_SELECTOR, 'a[data-testid="Heading"]')

    # Login locators
    PASS_INPUT = (By.NAME, 'password')
    EMAIL_INPUT = (By.NAME, 'email')

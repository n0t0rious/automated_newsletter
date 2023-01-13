from selenium.webdriver.common.by import By


class MainPageLocators:
    # Categories
    US_MARKETS = (By.CSS_SELECTOR, "button[data-id='/markets/us/']")
    # '/html/body/div[1]/div/main/div[5]/div/div[1]/div/ul'
    EU_MARKETS = (By.CSS_SELECTOR, "button[data-id='/markets/europe/']")
    # '/html/body/div[1]/div/main/div[5]/div/div[1]/div/ul'
    MACRO_MATTERs = (By.CSS_SELECTOR, "button[data-id='/markets/macromatters/']")
    # '/html/body/div[1]/div/main/div[4]/div/div[1]/div/ul'
    STOCKS = (By.CSS_SELECTOR, "button[data-id='/markets/stocks/']")
    # '/html/body/div[1]/div/div[3]/div[2]/div/div[1]/div/ul'
    DEALS = (By.CSS_SELECTOR, "button[data-id='/markets/deals/']")
    # '/html/body/div[1]/div/main/div[4]/ul'

    # Stories
    STORY_COLLECTIONS = (By.CLASS_NAME, "story-collection__three_columns__2Th0B story-collection__list__2M49i")

    # Login
    SIGN_IN = (By.XPATH, "//ul[contains(@class, 'story-collection__three_columns__2Th0B story-collection__list__2M49i')]")
    PASS_INPUT = (By.ID, 'password')
    EMAIL_INPUT = (By.ID, 'email')

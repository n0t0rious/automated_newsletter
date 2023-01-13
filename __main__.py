from scraping.scraper import Scraper
from scraping.locators import MainPageLocators as mP


def main():
    with Scraper(teardown=False) as scraper:
        scraper.land_first_page()
        scraper.select_category(*mP.US_MARKETS)
        scraper.get_content()


if __name__ == "__main__":
    main()

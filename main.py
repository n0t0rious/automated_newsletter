from scraping.scraper import Scraper
from scraping.locators import MainPageLocators as mP


def main():
    with Scraper(teardown=True) as scraper:
        scraper.land_first_page()
        scraper.select_category(*mP.MACRO_MATTERs)
        scraper.get_stories()


if __name__ == "__main__":
    main()

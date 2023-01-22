from scraping.scraper import Scraper
from scraping.locators import MainPageLocators as mP
from newsletter_gen.pdf_constructor import generate_newsletter


def main():
    with Scraper(teardown=True) as scraper:
        scraper.land_first_page()
        scraper.login()
        scraper.select_category(*mP.EU_MARKETS)
        contents = scraper.get_content()
        generate_newsletter(contents)


if __name__ == "__main__":
    main()

from packages.scraping.scraper import Scraper
from packages.newsletter_gen import generate_newsletter
from input_handler import get_input


def main():
    category, directory = get_input()
    with Scraper(teardown=True) as scraper:
        scraper.login()
        scraper.land_homepage()
        scraper.select_category(*category)
        contents = scraper.get_content()
        generate_newsletter(contents, directory=directory)


if __name__ == "__main__":
    main()

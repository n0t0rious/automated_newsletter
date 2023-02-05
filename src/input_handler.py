import os
from packages.scraping import MainPageLocators as mP


def get_input():
    categories = {
            'US_MARKETS': mP.US_MARKETS,
            'EU_MARKETS': mP.EU_MARKETS,
            'MACRO_MATTERS': mP.MACRO_MATTERS,
            'STOCKS': mP.STOCKS,
            'DEALS': mP.DEALS,
            'COMMODITIES': mP.COMMODITIES,
        }

    while True:
        category = input(f'select a category: {tuple(categories.keys())}\n').upper()
        if category not in categories.keys():
            print('Category was either inputted incorrectly or does not exist')
        else:
            break
    while True:
        directory = input(f'Specify directory path: ')
        if not os.path.isdir(directory):
            print('Directory was either inputted incorrectly or does not exist')
        else:
            break

    return categories[category], directory

import os


def retrieve_credentials():
    return os.environ.get("RU_MAIL"), os.environ.get("RU_PASS")

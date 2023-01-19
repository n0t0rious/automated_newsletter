import os


def retrieve_credentials():
    return os.environ.get("RU_PASS"), os.environ.get("RU_MAIL")

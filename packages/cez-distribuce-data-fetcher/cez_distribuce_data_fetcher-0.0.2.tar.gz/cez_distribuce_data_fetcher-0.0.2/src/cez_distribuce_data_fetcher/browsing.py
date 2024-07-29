from selenium.webdriver import ChromeOptions


def configure() -> ChromeOptions:
    options = ChromeOptions()
    options.add_argument(argument="--disable-gpu")
    options.add_argument(argument="--disable-dev-shm-usage")
    options.add_argument(argument="--headless")
    options.add_argument(argument="--no-sandbox")

    return options

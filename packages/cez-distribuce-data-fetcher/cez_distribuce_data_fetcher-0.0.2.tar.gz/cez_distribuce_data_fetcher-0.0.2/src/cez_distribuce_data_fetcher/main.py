import logging
import os
from datetime import datetime, timedelta

from selenium import webdriver

from cez_distribuce_data_fetcher import browsing, pnd
from cez_distribuce_data_fetcher.logger import LOGGER


def offset(target_time: datetime) -> datetime:
    offset = timedelta(hours=9)
    rounded_minutes = (target_time.minute // 15) * 15
    return (target_time - offset).replace(
        minute=rounded_minutes, second=0, microsecond=0
    )


def get_energy_measurements(
    from_time: datetime,
    pnd_device: str,
    pnd_password: str,
    pnd_user: str,
    to_time: datetime,
    pnd_url: str = "https://dip.cezdistribuce.cz/irj/portal/?zpnd=",
    remote_connection: bool = False,
    selenium_driver: str = "chromedriver",
    selenium_url: str = "http://localhost:4444",
) -> list[tuple[str, str, str]]:
    LOGGER.info(msg="Initializing the browser")
    options = browsing.configure()
    if remote_connection:
        LOGGER.info(msg="Connecting to the remote selenium server")
        browser = webdriver.Remote(command_executor=str(selenium_url), options=options)
    else:
        LOGGER.info(msg="Using the local selenium driver")
        options.binary_location = selenium_driver
        browser = webdriver.Chrome(options=options)

    LOGGER.info(msg=f"Opening the url {pnd_url}")
    browser.get(url=str(pnd_url))
    LOGGER.info(msg="Logging in")
    pnd.login(browser=browser, username=pnd_user, password=pnd_password)
    pnd.set_data_visualization(browser=browser)
    pnd.set_assembly(browser=browser)
    pnd.set_device(browser=browser, device=pnd_device)
    pnd.set_period(browser=browser)
    pnd.set_timerange(browser=browser, from_time=from_time, to_time=to_time)
    pnd.set_data_profile(browser=browser)
    measurements = pnd.get_measurements(browser=browser)
    return measurements


if __name__ == "__main__":
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(fmt=formatter)
    LOGGER.addHandler(hdlr=handler)

    today = datetime.now()
    yesterday = today - timedelta(days=4)

    pnd_device = os.environ["PND_DEVICE"]
    pnd_password = os.environ["PND_PASSWORD"]
    pnd_url = os.environ.get(
        "PND_URL", "https://dip.cezdistribuce.cz/irj/portal/?zpnd="
    )
    pnd_user = os.environ["PND_USER"]
    remote_connection = os.environ.get("REMOTE_CONNECTION", "False")
    remote_connection = remote_connection.lower() in ["true", "1", "yes"]
    selenium_driver = os.environ.get("SELENIUM_DRIVER", "chromedriver")
    selenium_url = os.environ.get("SELENIUM_URL", "http://localhost:4444")

    measurements = get_energy_measurements(
        from_time=offset(target_time=yesterday),
        pnd_device=pnd_device,
        pnd_password=pnd_password,
        pnd_url=pnd_url,
        pnd_user=pnd_user,
        remote_connection=remote_connection,
        selenium_driver=selenium_driver,
        selenium_url=selenium_url,
        to_time=offset(target_time=today),
    )
    for date, from_grid, to_grid in measurements:
        LOGGER.info(f"date: {date} | from_grid: {from_grid} | to_grid: {to_grid}")

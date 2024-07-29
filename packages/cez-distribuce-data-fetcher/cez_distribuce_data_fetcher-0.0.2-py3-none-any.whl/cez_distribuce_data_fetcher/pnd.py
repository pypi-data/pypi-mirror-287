from datetime import datetime, timedelta

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import Remote
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from cez_distribuce_data_fetcher.logger import LOGGER


def login(browser: Remote, username: str, password: str) -> None:
    username_placeholder = "Uživatelské jméno / e-mail"
    fill_in(string=username, browser=browser, placeholder=username_placeholder)
    password_placeholder = "Heslo"
    fill_in(string=password, browser=browser, placeholder=password_placeholder)

    try:
        loading_element = browser.find_element(By.TAG_NAME, "dip-loading")
    except NoSuchElementException:
        ...
    else:
        WebDriverWait(driver=browser, timeout=30).until(
            method=EC.staleness_of(element=loading_element)
        )
    select_by_xpath(
        expression='//*[@id="CybotCookiebotDialogBodyButtonDecline"]', browser=browser
    )
    login_text = "Přihlásit se"
    login_button = WebDriverWait(driver=browser, timeout=30).until(
        method=EC.element_to_be_clickable(
            mark=(By.XPATH, f'//button[normalize-space()="{login_text}"]')
        )
    )
    browser.execute_script("arguments[0].scrollIntoView();", login_button)
    login_button.click()


def select_by_xpath(expression: str, browser: Remote) -> None:
    element = WebDriverWait(driver=browser, timeout=30).until(
        method=EC.presence_of_element_located(locator=(By.XPATH, expression))
    )
    browser.execute_script("arguments[0].scrollIntoView();", element)
    browser.execute_script("arguments[0].click();", element)


def set_data_visualization(browser: Remote) -> None:
    title = "Tabulka dat"
    LOGGER.info(msg=f"Setting data visualization to '{title}'")
    select_by_xpath(expression="//button[@title='Tabulka dat']", browser=browser)


def set_assembly(browser: Remote) -> None:
    text = "Rychlá sestava"
    LOGGER.info(msg=f"Setting assembly to '{text}'")
    select_by_xpath(expression="//span[text()='Rychlá sestava']", browser=browser)


def set_device(browser: Remote, device: str) -> None:
    LOGGER.info(msg=f"Setting device to '{device}'")
    select_by_xpath(expression=f"//span[text()='{device}']", browser=browser)


def set_period(browser: Remote) -> None:
    period = "Vlastní"
    LOGGER.info(msg=f"Setting period to '{period}'")
    select_by_xpath(expression=f"//span[normalize-space()='{period}']", browser=browser)


def set_timerange(browser: Remote, from_time: datetime, to_time: datetime) -> None:
    LOGGER.info(msg=f"Setting timerange from '{from_time}' to '{to_time}'")
    time_placeholder = "Vyberte období"
    fill_in(
        string=f"{from_time:%d.%m.%Y %H:%M} - {to_time:%d.%m.%Y %H:%M}",
        browser=browser,
        placeholder=time_placeholder,
    )
    LOGGER.info(msg="Searching for data")
    search_button_text = "Vyhledat data"
    select_by_xpath(
        expression=f"//button[normalize-space()='{search_button_text}']",
        browser=browser,
    )


def set_data_profile(browser: Remote) -> None:
    title = "00 Profil spotřeby a výroby + Rv"
    LOGGER.info(msg=f"Setting data profile to '{title}'")
    select_by_xpath(
        expression="//*[contains(., '00 Profil spotřeby a výroby + Rv')]",
        browser=browser,
    )


def get_measurements(browser: Remote) -> list[tuple[str, str, str]]:
    LOGGER.info(msg="Getting table data")
    try:
        warning_box = WebDriverWait(driver=browser, timeout=2).until(
            method=EC.presence_of_element_located(
                locator=(
                    By.XPATH,
                    "//*[contains(., 'Pro zvolené období nejsou k dispozici žádná data')]",
                )
            )
        )
    except TimeoutException:
        pass
    else:
        if warning_box.text == "Pro zvolené období nejsou k dispozici žádná data":
            raise ValueError("No data found for selected period")
    measurements = []
    table = WebDriverWait(driver=browser, timeout=30).until(
        method=EC.presence_of_element_located(
            locator=(
                By.XPATH,
                '//table[starts-with(@id, "window-") and contains(@id, "-table-data")]',
            )
        )
    )

    pagination_input = browser.find_element(
        by=By.CLASS_NAME, value="pnd-pagination-number"
    )
    first_page = pagination_input.get_attribute(name="min")
    last_page = pagination_input.get_attribute(name="max")
    if first_page is None or last_page is None:
        raise ValueError("Unable to determine number of pages")
    for page in range(int(first_page), int(last_page) + 1):
        LOGGER.info(msg=f"Processing table page {page}")
        pagination_input.clear()
        pagination_input.send_keys(str(page))
        rows = table.find_elements(by=By.XPATH, value=".//tbody/tr")
        for row in rows:
            raw_date = row.find_element(by=By.XPATH, value=".//td[1]/div").text
            date = convert_date_format(raw_date=raw_date)
            from_grid_div = row.find_element(by=By.XPATH, value=".//td[2]/div")
            from_grid = get_measurement(div=from_grid_div, date=date)
            if not from_grid:
                continue
            to_grid_div = row.find_element(by=By.XPATH, value=".//td[3]/div")
            to_grid = get_measurement(div=to_grid_div, date=date)
            measurements.append((date, from_grid, to_grid))
    return measurements


def get_measurement(div: WebElement, date: datetime) -> float | None:
    match div.get_attribute("title"):
        case "naměřená data OK" | "naměřená data, výpadek napětí":
            return float(div.text.replace(",", "."))
        case "neplatná data":
            LOGGER.warning(
                msg=f"Data for {date} marked as 'neplatná data' (common during blackout)"
            )
            return 0.0
        case "nedefinovaný status":
            LOGGER.warning(msg=f"Data for {date} are not available")
            return None
        case _:
            status = div.get_attribute("title")
            raise ValueError(f"Unexpected status {status} for {date}")


def convert_date_format(raw_date: str) -> datetime:
    date_format = "%d.%m.%Y %H:%M"
    if "24:00" not in raw_date:
        return datetime.strptime(raw_date, date_format)
    raw_date = raw_date.replace("24:00", "00:00")
    return datetime.strptime(raw_date, date_format) + timedelta(days=1)


def fill_in(string: str, browser: Remote, placeholder: str) -> None:
    field = WebDriverWait(driver=browser, timeout=30).until(
        method=EC.presence_of_element_located(
            locator=(By.XPATH, f"//input[@placeholder='{placeholder}']")
        )
    )
    field.clear()
    field.send_keys(string)

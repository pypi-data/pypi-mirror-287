<!-- markdownlint-disable-file no-inline-html first-line-h1 -->
<div align="center">

# ČEZ Distribuce Data Fetcher<!-- omit from toc -->

![Python](https://img.shields.io/badge/python-3.10|3.11-3f7cad)
[![Ruff](https://img.shields.io/badge/linter-ruff-ef5552)](https://docs.astral.sh/ruff)
[![Mypy](https://img.shields.io/badge/typing-mypy-1F5082)](https://www.mypy-lang.org)

Fetches data from ČEZ Distribuce Portal naměřených dat.

</div>

## How to use

- Install from pip
  
  ```bash
  pip install cez-distribution-data-fetcher
  ```

- Use `get_energy_measurements()` function
  ```python
  from datetime import datetime, timedelta

  from cez_distribuce_data_fetcher import get_energy_measurements, offset

  today = datetime.now()
  yesterday = today - timedelta(days=1)

  pnd_device = "ELM 777777"
  pnd_password = "SECRET"
  pnd_user = "USERNAME"

  measurements = get_energy_measurements(
      from_time=offset(target_time=yesterday),
      pnd_device=pnd_device,
      pnd_password=pnd_password,
      pnd_user=pnd_user,
      to_time=offset(target_time=today),
  )
  for date, from_grid, to_grid in measurements:
      print(f"date: {date} | from_grid: {from_grid} | to_grid: {to_grid}")
  ```

## API

### `get_energy_measurements()`

This function gets energy consumption and energy creation measurements from ČEZ Distribuce PND. It returns tuple with **date**, **from grid** and **to grid** measurements. 

Following parameters are available:

| Parameter       | Description   |
| --------------- | ------------- |
| from_time       | The starting time for fetching energy measurements. |
| pnd_device      | The device identifier (eg `ELM 777777`). |
| pnd_password    | The password for accessing the ČEZ Distribuce Portal. |
| pnd_user        | The username for accessing the ČEZ Distribuce Portal. |
| pnd_url         | The URL of the ČEZ Distribuce Portal. Default value is "https://dip.cezdistribuce.cz/irj/portal/?zpnd=". |
| to_time         | The ending time for fetching energy measurements. |
| remote_connection | A boolean value indicating whether to use a remote connection for Selenium. Default value is False. |
| selenium_driver | The driver for Selenium. Default value is "chromedriver". |
| selenium_url    | The URL for Selenium. Default value is "http://localhost:4444". |

To see more about how to configure Selenium, check out [How to configure Selenium](#how-to-configure-selenium) section.

### `offset()`

Data availabe in the ČEZ Distribuce Portal are not live. They have 8-9 hours offset. This function is a helper utility to set this offset for provided `from_time` and `to_time` parameters. 

## How to configure Selenium

As ČEZ Distribuce Portal does not offer publicly accesible API, the Selenium framework is used to scrape the data. Selenium needs a browser to work (only Chromium is supported). There are two methods available:

1) Remote (**recommended**)
   - Use [docker-selenium](https://github.com/SeleniumHQ/docker-selenium) to start Selenium browser in a container.
     ```bash
     docker run --rm -it -p 4444:4444 -p 5900:5900 -p 7900:7900 --shm-size 2g selenium/standalone-chromium:latest
     ```
    - Set `remote_connection` to `True` and optionally update `selenium_url` (defaults to `http://localhost:4444`).

2) Local
    - Set `remote_connection` to `False` (default value) and optionally update `selenium_driver` path (defaults to `chromedriver`).
    - Chromedriver binaries are available [here](https://developer.chrome.com/docs/chromedriver/downloads).

## Changelog 📝

See [release notes](https://github.com/aka-raccoon/cez-distribution-data-fetcher/releases).

## How to contribute ✌

Every contribution is much appreciated.

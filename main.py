from enum import Enum

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class Browser(Enum):
    CHROME = "Chrome"
    FIREFOX = "Firefox"
    IE = "Ie"


class CustomizerWebDriver:
    def __new__(cls, browser: Browser, driver_path: str | None = None, *args, **kwargs):
        _b = getattr(webdriver, browser.value)
        driver: WebDriver = _b(driver_path)
        return driver


if __name__ == "__main__":
    _browser = Browser.CHROME

    d = CustomizerWebDriver(browser=_browser)
    d.get("https://www.google.com")

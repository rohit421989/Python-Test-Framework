from selenium import webdriver

from config.ui_config import UIConfig


class BrowserFactory:

    @staticmethod
    def create_browser():

        browser = UIConfig.BROWSER

        if browser == "chrome":

            options = webdriver.ChromeOptions()

            if UIConfig.HEADLESS:
                options.add_argument("--headless=new")

            driver = webdriver.Chrome(
                options=options
            )

        elif browser == "firefox":

            options = webdriver.FirefoxOptions()

            if UIConfig.HEADLESS:
                options.add_argument("--headless")

            driver = webdriver.Firefox(
                options=options
            )

        else:

            raise ValueError(
                f"Unsupported browser: {browser}"
            )

        driver.maximize_window()

        return driver
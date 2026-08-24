from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from config.ui_config import UIConfig


class BrowserFactory:

    @staticmethod
    def create_browser():

        if UIConfig.BROWSER == "chrome":

            options = Options()

            if UIConfig.HEADLESS:
                options.add_argument("--headless=new")

            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")

            # Chromium binary inside Docker
            options.binary_location = "/usr/bin/chromium"

            # Chromium driver inside Docker
            service = Service(
                "/usr/bin/chromedriver"
            )

            driver = webdriver.Chrome(
                service=service,
                options=options
            )

            return driver

        elif UIConfig.BROWSER == "firefox":

            options = webdriver.FirefoxOptions()

            if UIConfig.HEADLESS:
                options.add_argument("--headless")

            return webdriver.Firefox(
                options=options
            )

        raise ValueError(
            f"Unsupported browser: {UIConfig.BROWSER}"
        )




# from selenium import webdriver

# from config.ui_config import UIConfig


# class BrowserFactory:

#     @staticmethod
#     def create_browser():

#         browser = UIConfig.BROWSER

#         if browser == "chrome":

#             options = webdriver.ChromeOptions()

#             if UIConfig.HEADLESS:
#                 options.add_argument("--headless=new")

#             driver = webdriver.Chrome(
#                 options=options
#             )

#         elif browser == "firefox":

#             options = webdriver.FirefoxOptions()

#             if UIConfig.HEADLESS:
#                 options.add_argument("--headless")

#             driver = webdriver.Firefox(
#                 options=options
#             )

#         else:

#             raise ValueError(
#                 f"Unsupported browser: {browser}"
#             )

#         driver.maximize_window()

#         return driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logging.logger import Logger


class BasePage:

    def __init__(self, driver, timeout=10):

        self.logger = Logger.get_logger(
        self.__class__.__name__
    )

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            timeout
            
        )

    def click(self, locator):

        self.logger.info(
        f"Clicking element: {locator}"
        )

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
    )

        element.click()

    def enter_text(self, locator, text):

        self.logger.info(
        f"Entering text into: {locator}"
        )

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        element.clear()
        element.send_keys(text)

    def get_text(self, locator):

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        return element.text

    def is_visible(self, locator):

        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).is_displayed()

    def wait_for_url(self, url):

        self.wait.until(
            EC.url_to_be(url)
        )

    def get_title(self):

        return self.driver.title

    def get_current_url(self):

        return self.driver.current_url

    def get_attribute(self, locator, attribute):

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        return element.get_attribute(attribute)

    def scroll_to_element(self, locator):

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            element
        )

    def wait_for_element(self, locator):

        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )
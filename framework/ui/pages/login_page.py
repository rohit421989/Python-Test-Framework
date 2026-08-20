from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from framework.ui.pages.secure_area_page import SecureAreaPage

from framework.ui.base_page import BasePage


class LoginPage(BasePage):

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def enter_username(self, username):

        self.enter_text(
            self.USERNAME,
            username
        )

    def enter_password(self, password):

        self.enter_text(
            self.PASSWORD,
            password
        )

    def click_login(self):

        self.click(
            self.LOGIN_BUTTON
        )

    def login(self, username, password):

        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

        return SecureAreaPage(self.driver)
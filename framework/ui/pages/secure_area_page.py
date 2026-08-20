from selenium.webdriver.common.by import By

from framework.ui.base_page import BasePage


class SecureAreaPage(BasePage):

    SECURE_AREA_HEADER = (
        By.CSS_SELECTOR,
        "h2"
    )

    def is_secure_area_displayed(self):

        return self.is_visible(
            self.SECURE_AREA_HEADER
        )

    def get_header_text(self):

        return self.get_text(
            self.SECURE_AREA_HEADER
        )
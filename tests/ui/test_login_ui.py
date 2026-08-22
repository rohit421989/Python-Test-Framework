import pytest

from framework.ui.pages.login_page import LoginPage
from config.ui_config import UIConfig
from framework.ui.pages.login_page import LoginPage
import allure
import pytest

@allure.feature("Authentication")
@allure.story("User Login")
@allure.title("User can login with valid credentials")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.ui
def test_valid_login(browser):

    login_page = LoginPage(browser)
    with allure.step("Open login page"):
        login_page.open(
            UIConfig.LOGIN_URL
    )
    with allure.step("Verify login page"):
        assert login_page.is_login_page_displayed()

    with allure.step("Login with valid credentials"):
        secure_area_page = login_page.login(
            "tomsmith",
            "SuperSecretPassword!"
    )
    with allure.step("Verify secure area"):
        assert secure_area_page.is_secure_area_displayed()

    assert (
        secure_area_page.get_header_text()
        == "Secure Area"
    )


def get_error_message(self):

    return self.get_text(
        self.FLASH_MESSAGE
    )
    
@allure.feature("Authentication")
@allure.story("User Login")
@allure.title("User cannot login with invalid credentials")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.ui
def test_invalid_login(browser):
    login_page = LoginPage(browser)

    login_page.open(
        UIConfig.LOGIN_URL
    )

    login_page.login(
        "wrong_user",
        "wrong_password"
    )

    assert (
        "Your username is invalid!"
        in login_page.get_error_message()
    )

  
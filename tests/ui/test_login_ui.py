import pytest

from framework.ui.pages.login_page import LoginPage


@pytest.mark.ui
def test_valid_login(browser):

    browser.get(
        "https://the-internet.herokuapp.com/login"
    )

    login_page = LoginPage(browser)

    assert login_page.is_login_page_displayed()

    secure_area_page = login_page.login(
        "tomsmith",
        "SuperSecretPassword!"
    )

    assert secure_area_page.is_secure_area_displayed()

    assert (
        secure_area_page.get_header_text()
        == "Secure Area"
    )


@pytest.mark.ui
def test_invalid_login(browser):

    browser.get(
        "https://the-internet.herokuapp.com/login"
    )

    login_page = LoginPage(browser)

    login_page.login(
        "wrong_user",
        "wrong_password"
    )

    assert (
        "Your username is invalid!"
        in login_page.get_error_message()
    )
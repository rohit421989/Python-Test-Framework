import pytest

from config.ui_config import UIConfig
from framework.api.user_data_api import UserDataAPI
from framework.ui.pages.login_page import LoginPage


@pytest.mark.integration
def test_api_data_with_ui(
    api_client,
    browser
):

    # -------------------------
    # API layer
    # -------------------------

    user_data_api = UserDataAPI(
        api_client
    )

    response = user_data_api.get_user(1)

    assert response.status_code == 200

    user = response.json()

    assert user["id"] == 1

    # -------------------------
    # UI layer
    # -------------------------

    login_page = LoginPage(browser)

    login_page.open(
        UIConfig.LOGIN_URL
    )

    assert login_page.is_login_page_displayed()

    secure_area_page = login_page.login(
        "tomsmith",
        "SuperSecretPassword!"
    )

    assert secure_area_page.is_secure_area_displayed()
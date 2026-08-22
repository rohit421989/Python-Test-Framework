import pytest


from config.config import Config
from framework.api.api_client import APIClient
from framework.database.db_client import DBClient
from framework.utilities.screenshot import (ScreenshotUtil)
from selenium import webdriver
from framework.ui.browser_factory import BrowserFactory


@pytest.fixture
def login_credentials():
    return {
        "username": "admin",
        "password": "admin123"
    }


@pytest.fixture
def test_user():
    print("\n Creating test user")

    user={
        "username": "testuser",
        "email": "test@example.com"
    }

    yield user
    print("\n Deleting test user")
    #yield is just like return with added feature when the subsequent lines after yield get executed after the calling function has run


@pytest.fixture
def api_client():

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Config.API_TOKEN}"
    }

    return APIClient(
        base_url=Config.get_base_url(),
        headers=headers
    )


@pytest.fixture
def db_client():

    client = DBClient(
        "sqlite:///test.db"
    )

    yield client

    client.close()


@pytest.fixture
def clean_users_table(db_client):

    db_client.execute_update(
        """
        DROP TABLE IF EXISTS users
        """
    )

    yield

    db_client.execute_update(
        """
        DROP TABLE IF EXISTS users
        """
    )    

import pytest

from selenium import webdriver


@pytest.fixture
def browser():

    driver = webdriver.Chrome()

    yield driver

    driver.quit()



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    setattr(
        item,
        "rep_" + report.when,
        report
    )


@pytest.fixture
def browser(request):

    driver = webdriver.Chrome()

    driver.maximize_window()

    yield driver

    if request.node.rep_call.failed:

        ScreenshotUtil.capture(
            driver,
            request.node.name
        )

    driver.quit()


@pytest.fixture
def browser(request):

    driver = BrowserFactory.create_browser()

    yield driver
    try:
        if request.node.rep_call.failed:

            ScreenshotUtil.capture(
                driver,
                request.node.name
        )
    finally:
        driver.quit()
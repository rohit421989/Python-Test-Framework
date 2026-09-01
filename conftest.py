import pytest
import allure
import os

from config.config import Config
from framework.api.api_client import APIClient
from framework.database.db_client import DBClient
from framework.ui.browser_factory import BrowserFactory
from framework.utilities.screenshot import ScreenshotUtil
from framework.services.user_service import UserService
from pathlib import Path


@pytest.fixture
def login_credentials():

    return {
        "username": "admin",
        "password": "admin123"
    }


@pytest.fixture
def test_user():

    print("\nCreating test user")

    user = {
        "username": "testuser",
        "email": "test@example.com"
    }

    yield user

    print("\nDeleting test user")


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
def db_client(request):

    worker_id = getattr(
        request.config,
        "workerinput",
        {}
    ).get(
        "workerid",
        "master"
    )

    database_name = f"test_{worker_id}.db"

    client = DBClient(
        f"sqlite:///{database_name}"
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
#def browser(request):

    # driver = BrowserFactory.create_browser()

    # yield driver

    # try:

    #     if getattr(
    #         request.node,
    #         "rep_call",
    #         None
    #     ) and request.node.rep_call.failed:

    #         # Save screenshot using existing framework utility
    #         ScreenshotUtil.capture(
    #             driver,
    #             request.node.name
    #         )

    #         # Attach screenshot directly to Allure
    #         allure.attach(
    #             driver.get_screenshot_as_png(),
    #             name="Failure Screenshot",
    #             attachment_type=allure.attachment_type.PNG
    #         )

    # finally:

    #     driver.quit()

def browser(request):

    driver = BrowserFactory.create_browser()

    yield driver

    try:

        if getattr(
            request.node,
            "rep_call",
            None
        ) and request.node.rep_call.failed:

            # Screenshot
            ScreenshotUtil.capture(
                driver,
                request.node.name
            )

            # Allure screenshot
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            # Allure log

            worker_id = os.getenv(
                "PYTEST_XDIST_WORKER",
                "master"
)
            log_file = Path(
                f"reports/logs/test_execution_{worker_id}.log"
            )

            if log_file.exists():

                allure.attach.file(
                    str(log_file),
                    name=f"Execution Log - {worker_id}",
                    attachment_type=allure.attachment_type.TEXT
                )

    finally:

        driver.quit()


@pytest.fixture
def user_service(api_client):

    return UserService(
        api_client
    )







###################################################################
#Old conftest file with all the fixtures and hooks for pytest
###################################################################

# import pytest


# from config.config import Config
# from framework.api.api_client import APIClient
# from framework.database.db_client import DBClient
# from framework.utilities.screenshot import (ScreenshotUtil)
# from selenium import webdriver
# from framework.ui.browser_factory import BrowserFactory


# @pytest.fixture
# def login_credentials():
#     return {
#         "username": "admin",
#         "password": "admin123"
#     }


# @pytest.fixture
# def test_user():
#     print("\n Creating test user")

#     user={
#         "username": "testuser",
#         "email": "test@example.com"
#     }

#     yield user
#     print("\n Deleting test user")
#     #yield is just like return with added feature when the subsequent lines after yield get executed after the calling function has run


# @pytest.fixture
# def api_client():

#     headers = {
#         "Accept": "application/json",
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {Config.API_TOKEN}"
#     }

#     return APIClient(
#         base_url=Config.get_base_url(),
#         headers=headers
#     )


# @pytest.fixture
# def db_client():

#     client = DBClient(
#         "sqlite:///test.db"
#     )

#     yield client

#     client.close()


# @pytest.fixture
# def clean_users_table(db_client):

#     db_client.execute_update(
#         """
#         DROP TABLE IF EXISTS users
#         """
#     )

#     yield

#     db_client.execute_update(
#         """
#         DROP TABLE IF EXISTS users
#         """
#     )    

# import pytest

# from selenium import webdriver


# # @pytest.fixture
# # def browser():

# #     driver = webdriver.Chrome()

# #     yield driver

# #     driver.quit()



# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):

#     outcome = yield

#     report = outcome.get_result()

#     setattr(
#         item,
#         "rep_" + report.when,
#         report
#     )


# # @pytest.fixture
# # def browser(request):

# #     driver = webdriver.Chrome()

# #     driver.maximize_window()

# #     yield driver

# #     if request.node.rep_call.failed:

# #         ScreenshotUtil.capture(
# #             driver,
# #             request.node.name
# #         )

# #     driver.quit()


# @pytest.fixture
# def browser(request):

#     driver = BrowserFactory.create_browser()
#     driver.maximize_window()
    

#     yield driver
#     try:
#         if request.node.rep_call.failed:

#             ScreenshotUtil.capture(
#                 driver,
#                 request.node.name
#         )
#     finally:
#         driver.quit()
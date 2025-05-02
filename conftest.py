import allure
import pytest
import shutil
import os
import logging


from config import settings as settings
from data.users_credentials import existing_credentials, low_access_credentials
from helpers.cleanup import delete_user_by_login
from services.api_users_service import ApiUsersService

@pytest.fixture(scope="session", autouse=True)
@allure.title("Creating users.json from template")
def create_users_jsons():
    if not os.path.exists(settings.USERS_PATH):
        shutil.copy(settings.USERS_TEMPLATE_PATH, settings.USERS_PATH)
    logging.info("Creating users.json")

@pytest.fixture(scope="session",autouse=True)
@allure.title("Creating dashboards.json from template")
def create_dashboards_jsons():
    if not os.path.exists(settings.DASHBOARDS_PATH):
        shutil.copy(settings.DASHBOARDS_TEMPLATE_PATH, settings.DASHBOARDS_PATH)
    logging.info("Creating dashboards.json")

@pytest.fixture(scope="session",autouse=True)
@allure.title("Creating user with low access for tests")
def create_low_access_user():
    try:
        response = ApiUsersService.create_api_user(low_access_credentials)
        if response.status_code != 200:
            pytest.exit(f"Failed to create LowAccessUser with response code - {response.status_code}")
        logging.info("Creating Low Access User")
    except Exception as e:
        logging.critical(f"Exception during LowAccessUser creation: {e}")
        pytest.exit(f"Critical error in fixture: stopping test execution")

@pytest.fixture(scope="session",autouse=True)
@allure.title("Creating existing user for tests")
def create_existing_user():
    try:
        response = ApiUsersService.create_api_user(existing_credentials)
        if response.status_code != 200:
            pytest.exit(f"Failed to create ExistingUser with response code - {response.status_code}")
        logging.info("Creating Existing User")
    except Exception as e:
        logging.critical(f"Exception during ExistingUser creation: {e}")
        pytest.exit(f"Critical error in fixture: stopping test execution")

@allure.title("Delete users from previously steps accross pytest hook")
def pytest_sessionfinish(session, exitstatus):
    delete_user_by_login(existing_credentials)
    delete_user_by_login(low_access_credentials)
    logging.info("Cleaning up is done")

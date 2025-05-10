import allure
import pytest
import shutil
import os
import logging

from config import settings as settings
from data.users_credentials import existing_credentials, low_access_credentials, organizations_user
from services.api_dashboards_service import ApiDashboardsService
from services.api_organizations_service import ApiOrganizationsService
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
@allure.title("Creating organizations.json from template")
def create_dashboards_jsons():
    if not os.path.exists(settings.ORGANIZATIONS_PATH):
        shutil.copy(settings.ORGANIZATIONS_TEMPLATE_PATH, settings.ORGANIZATIONS_PATH)
    logging.info("Creating organizations.json")

@pytest.fixture(scope="session",autouse=True)
@allure.title("Creating new organization")
def create_new_organization():
    response,org_id = ApiOrganizationsService.create_new_organization()

    assert response.status_code == 200, f'Expected status code 200, got {response.status_code}'
    assert response.json().get('orgId') == org_id
    assert response.json().get('message') == 'Organization created'

@pytest.fixture(scope="session",autouse=True)
@allure.title("Creating folder for dashboard")
def _create_folder_for_dashboard():
    response = ApiDashboardsService.create_folder()

    assert response.status_code == 200, f'Expected status code 200, got {response.status_code}'
    assert response.json().get('title') == 'Folder for API Test'

@pytest.fixture(scope="session",autouse=True)
@allure.title("Creating dashboard")
def _create_dashboard(_create_folder_for_dashboard):
    response = ApiDashboardsService.create_dashboard()
    assert response.status_code == 200, f'Expected status code 200, got {response.status_code}'


@pytest.fixture(scope="session",autouse=True)
@allure.title("Creating user with low access for tests")
def create_low_access_user():
    try:
        response = ApiUsersService.create_api_user(low_access_credentials)
        if response.status_code != 200:
            pytest.exit(f"Failed to create LowAccessUser with response code - {response.status_code}")

        userid = response.json().get('id')
        ApiOrganizationsService.delete_user_from_org(userid = userid)
        logging.info(f'User {userid} deleted from org')

        logging.info("Creating Low Access User")
    except Exception as e:
        logging.critical(f"Exception during LowAccessUser creation: {e}")
        pytest.exit(f"Critical error in fixture: stopping test execution")

@pytest.fixture(scope="session",autouse=True)
@allure.title("Creating organizations_user for tests")
def create_organizations_user():
    try:
        response = ApiUsersService.create_api_user(organizations_user)
        if response.status_code != 200:
            pytest.exit(f"Failed to create organizations_user with response code - {response.status_code}")
        logging.info("Creating organizations_user")
    except Exception as e:
        logging.critical(f"Exception during organizations_user creation: {e}")
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

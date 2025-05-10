import os
import logging

from data.users_credentials import existing_credentials, low_access_credentials, organizations_user
from helpers.cleanup import delete_user_by_login
from services.api_dashboards_service import ApiDashboardsService
from services.api_organizations_service import ApiOrganizationsService


def pytest_configure(config):
    config.addinivalue_line("markers", "NegativeApi")
    config.addinivalue_line("markers", "PositiveApi")

def pytest_sessionstart(session):
    env_path = os.path.join(os.getcwd(), 'allure-results', 'environment.properties')
    os.makedirs(os.path.dirname(env_path), exist_ok=True)
    with open(env_path, 'w') as f:
        f.write("Python=3.11\n")
        f.write("BaseURL=http://grafana:3000\n")
        f.write("Runner=GitHub Actions\n")

def pytest_sessionfinish(session, exitstatus):
    delete_user_by_login(existing_credentials)
    delete_user_by_login(low_access_credentials)
    delete_user_by_login(organizations_user)
    ApiDashboardsService.delete_dashboard()
    ApiDashboardsService.delete_folder_for_dashboard()
    ApiOrganizationsService.delete_organization()
    logging.info("Cleaning up is done")

import allure
import pytest

from services.api_dashboards_service import ApiDashboardsService

@allure.title("Test create new folder for dashboard")
@allure.description("This test attempt to create a new folder for dashboard")
@allure.tag("ApiDashboardsService", "Positive")
@pytest.mark.PositiveApi
def test_create_folder_for_dashboard():

    response = ApiDashboardsService.create_folder()

    assert response.status_code == 200, f'Expected status code 200, got {response.status_code}'
    assert response.json().get('title') == 'Folder for API Test'

@allure.title("Test create new  dashboard in folder")
@allure.description("This test attempt to create the new dashboard in folder")
@allure.tag("ApiDashboardsService", "Positive")
@pytest.mark.PositiveApi
def test_create_dashboard_in_folder():

    response = ApiDashboardsService.create_dashboard()
    assert response.status_code == 200, f'Expected status code 200, got {response.status_code}'

@allure.title("Test get dashboard in folder")
@allure.description("This test attempt to get the dashboard in folder")
@allure.tag("ApiDashboardsService", "Positive")
@pytest.mark.PositiveApi
def test_get_dashboard():
    response, title = ApiDashboardsService.get_dashboard()
    assert title == 'Dashboard for API'
    assert response.status_code == 200, f'Expected status code 200, got {response.status_code}'
    assert response.json().get("dashboard",{}).get("title") == title

@allure.title("Test delete dashboard from folder")
@allure.description("This test attempt delete the dashboard from folder")
@allure.tag("ApiDashboardsService", "Positive")
@pytest.mark.PositiveApi
def test_delete_dashboard_in_folder():
    response,title = ApiDashboardsService.delete_dashboard()

    assert response.status_code == 200, f'Expected status code 200, got {response.status_code}'
    assert response.json().get('title') == title
    assert response.json().get('message') == f'Dashboard {title} deleted'

@allure.title("Test delete dashboard  folder")
@allure.description("This test attempt delete the dashboard folder")
@allure.tag("ApiDashboardsService", "Positive")
@pytest.mark.PositiveApi
def test_delete_folder_for_dashboard():
    response = ApiDashboardsService.delete_folder_for_dashboard()

    assert response.status_code == 200, f'Expected status code 200, got {response.status_code}'
    assert response.json().get('message') == 'Folder deleted'



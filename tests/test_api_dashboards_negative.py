import allure
import pytest

from services.api_dashboards_service import ApiDashboardsService

@allure.title("Test get dashboard with incorrect data for auth")
@allure.description("This test attempt get dashboard with incorrect data for auth")
@allure.tag("ApiDashboardsService", "Negative")
@allure.id("get_dashboard_with_incorrect_auth")
@pytest.mark.NegativeApi
def test_get_dashboard_with_incorrect_auth():
    response = ApiDashboardsService.get_dashboard_with_incorrect_auth()
    assert response.status_code == 401, f'Expected status code 401, got {response.status_code}'

@allure.title("Test get dashboard from user with low access in the system")
@allure.description("This test attempt get dashboard from user with low access in the system")
@allure.tag("ApiDashboardsService", "Negative")
@allure.id("get_dashboard_with_low_level_access")
@pytest.mark.NegativeDashboard
def test_get_dashboard_with_low_level_access():
    response = ApiDashboardsService.get_dashboard_with_low_level_access()
    assert response.status_code == 403, f'Expected status code 403, got {response.status_code}'

@allure.title("Test get 404 dashboard")
@allure.description("This test attempt get 404 dashboard")
@allure.tag("ApiDashboardsService", "Negative")
@allure.id("get_404_dashboard")
@pytest.mark.NegativeApi
def test_get_404_dashboard():
    response = ApiDashboardsService.get_404_dashboard()
    assert response.status_code == 404, f'Expected status code 404, got {response.status_code}'
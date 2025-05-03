import allure
import pytest

from services.api_dashboards_service import ApiDashboardsService

@allure.title("Test get dashboard in folder")
@allure.description("This test attempt to get the dashboard in folder")
@allure.tag("ApiDashboardsService", "Positive")
@allure.id("get_dashboard")
@pytest.mark.PositiveApi
def test_get_dashboard():
    response, title = ApiDashboardsService.get_dashboard()
    assert title == 'Dashboard for API'
    assert response.status_code == 200, f'Expected status code 200, got {response.status_code}'
    assert response.json().get("dashboard",{}).get("title") == title




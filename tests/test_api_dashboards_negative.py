import pytest

from services.api_dashboards_service import ApiDashboardsService


@pytest.mark.NegativeDashboard
def test_get_dashboard_with_incorrect_auth():
    response = ApiDashboardsService.get_dashboard_with_incorrect_auth()
    assert response.status_code == 401, f'Expected status code 401, got {response.status_code}'

@pytest.mark.NegativeDashboard
def test_get_dashboard_with_low_level_access():
    response = ApiDashboardsService.get_dashboard_with_low_level_access()
    assert response.status_code == 403, f'Expected status code 403, got {response.status_code}'

@pytest.mark.NegativeDashboard
def test_get_404_dashboard():
    response = ApiDashboardsService.get_404_dashboard()
    assert response.status_code == 404, f'Expected status code 404, got {response.status_code}'
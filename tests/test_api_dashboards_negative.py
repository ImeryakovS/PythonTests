import allure
import pytest

from helpers.schemas.dashboards_schema import GetDashboardsWithIncorrectCredentialsSchema
from helpers.schemas.user_schema import GetDashboardWithLowAccessSchema, Get404DashboardSchema
from services.api_dashboards_service import ApiDashboardsService
from services.utils import validate_status_code_and_body


@allure.title("Test get dashboard with incorrect data for auth")
@allure.description("This test attempt get dashboard with incorrect data for auth")
@allure.tag("ApiDashboardsService", "Negative")
@allure.id("get_dashboard_with_incorrect_auth")
@pytest.mark.NegativeApi
def test_get_dashboard_with_incorrect_auth():
    response = ApiDashboardsService.get_dashboard_with_incorrect_auth()
    validate_status_code_and_body(response, GetDashboardsWithIncorrectCredentialsSchema, 401)

@allure.title("Test get dashboard from user with low access in the system")
@allure.description("This test attempt get dashboard from user with low access in the system")
@allure.tag("ApiDashboardsService", "Negative")
@allure.id("get_dashboard_with_low_level_access")
@pytest.mark.NegativeDashboard
def test_get_dashboard_with_low_level_access():
    response = ApiDashboardsService.get_dashboard_with_low_level_access()
    validate_status_code_and_body(response, GetDashboardWithLowAccessSchema, 403)

@allure.title("Test get 404 dashboard")
@allure.description("This test attempt get 404 dashboard")
@allure.tag("ApiDashboardsService", "Negative")
@allure.id("get_404_dashboard")
@pytest.mark.NegativeApi
def test_get_404_dashboard():
    response = ApiDashboardsService.get_404_dashboard()
    validate_status_code_and_body(response, Get404DashboardSchema, 404)
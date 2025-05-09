import allure
import pytest

from helpers.schemas.dashboards_schema import GetDashboardSchema
from services.api_dashboards_service import ApiDashboardsService
from services.utils import validate_status_code_and_body


@allure.title("Test get dashboard in folder")
@allure.description("This test attempt to get the dashboard in folder")
@allure.tag("ApiDashboardsService", "Positive")
@allure.id("get_dashboard")
@pytest.mark.PositiveApi
def test_get_dashboard():
    response, title = ApiDashboardsService.get_dashboard()
    validate_status_code_and_body(response, GetDashboardSchema, 200, path=["dashboard"])




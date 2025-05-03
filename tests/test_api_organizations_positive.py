import allure
import pytest

from services.api_organizations_service import ApiOrganizationsService


@allure.title("Test add new user in organization")
@allure.description("This test attempt to add new user in organization")
@allure.tag("ApiOrganizationsService", "Positive")
@allure.id("add_user_in_organization")
@pytest.mark.PositiveApi
def test_add_user_in_organization():
    response,user_id = ApiOrganizationsService.add_user_in_organization()

    assert response.json().get("message") == "User added to organization"
    assert response.json().get("userId") == user_id





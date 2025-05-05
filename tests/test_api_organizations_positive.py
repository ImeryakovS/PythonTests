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

    assert response.status_code == 200, f'Expected status code 200, got {response.status_code} - {response.json().get('message', '')}'
    assert response.json().get("message") == "User added to organization"
    assert response.json().get("userId") == user_id

@allure.title("Test get organizations by id")
@allure.description("This test attempt get organizations by id")
@allure.tag("ApiOrganizationsService", "Positive")
@allure.id("get_organizations_by_id")
@pytest.mark.PositiveApi
def test_get_organizations_by_id():
    response,org_id,name_org = ApiOrganizationsService.get_organizations_by_id()

    assert response.status_code == 200, f'Expected status code 200, got {response.status_code} - {response.json().get('message', '')}'
    assert response.json().get("id") == org_id
    assert response.json().get("name") == name_org

@allure.title("Test update user permissions in org")
@allure.description("This test attempt update user permissions in org")
@allure.tag("ApiOrganizationsService", "Positive")
@allure.id("update_user_in_org")
@pytest.mark.PositiveApi
def test_update_user_in_org():
    response = ApiOrganizationsService.update_user_in_org()

    assert response.status_code == 200, f'Expected status code 200, got {response.status_code} - {response.json().get('message', '')}'
    assert response.json().get("message") == "Organization user updated"







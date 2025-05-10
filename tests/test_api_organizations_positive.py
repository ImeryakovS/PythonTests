import allure
import pytest

from helpers.schemas.organizations_schema import AddUserInOrganizations, GetOrganizationsById, UpdateUserInOrg
from services.api_organizations_service import ApiOrganizationsService
from services.utils import validate_status_code_and_body


@allure.title("Test add new user in organization")
@allure.description("This test attempt to add new user in organization")
@allure.tag("ApiOrganizationsService", "Positive")
@allure.id("add_user_in_organization")
@pytest.mark.PositiveApi
def test_add_user_in_organization():
    response,user_id = ApiOrganizationsService.add_user_in_organization()
    validate_status_code_and_body(response, AddUserInOrganizations, 200)

@allure.title("Test get organizations by id")
@allure.description("This test attempt get organizations by id")
@allure.tag("ApiOrganizationsService", "Positive")
@allure.id("get_organizations_by_id")
@pytest.mark.PositiveApi
def test_get_organizations_by_id():
    response,org_id,name_org = ApiOrganizationsService.get_organizations_by_id()
    validate_status_code_and_body(response, GetOrganizationsById, 200)


@allure.title("Test update user permissions in org")
@allure.description("This test attempt update user permissions in org")
@allure.tag("ApiOrganizationsService", "Positive")
@allure.id("update_user_in_org")
@pytest.mark.PositiveApi
def test_update_user_in_org():
    response = ApiOrganizationsService.update_user_in_org()
    validate_status_code_and_body(response, UpdateUserInOrg, 200)







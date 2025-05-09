import allure
import pytest
from pydantic.v1.schema import schema

from data.users_credentials import credentials
from helpers.schemas.user_schema import CreateUserSchema, ChangeUserPassword, DeleteUserSchema
from services.api_users_service import ApiUsersService
from services.utils import assert_status_message, validate_status_code_and_body


@allure.title("Test create API user")
@allure.description("This test attempt create new user with credentials")
@allure.tag("APIUsersService", "Positive")
@allure.id("create_user")
@pytest.mark.PositiveApi
def test_create_user():
    response = ApiUsersService.create_api_user(credentials)
    validate_status_code_and_body(response, CreateUserSchema, 200)

@allure.title("Test change API user password")
@allure.description("This test attempt change password for last created user")
@allure.tag("APIUsersService", "Positive")
@allure.id("change_user_password")
@pytest.mark.PositiveApi
def test_change_user_password():
    response = ApiUsersService.change_user_password()
    validate_status_code_and_body(response, ChangeUserPassword, 200)

@allure.title("Test delete API user password")
@allure.description("This test attempt delete last created user")
@allure.tag("APIUsersService", "Positive")
@allure.id("delete_user")
@pytest.mark.PositiveApi
def test_delete_user():
    response = ApiUsersService.delete_api_user()
    validate_status_code_and_body(response, DeleteUserSchema, 200)








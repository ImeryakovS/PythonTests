import allure
import pytest

from data.users_credentials import credentials
from services.api_users_service import ApiUsersService
from services.utils import assert_status_message

@allure.title("Test create API user")
@allure.description("This test attempt create new user with credentials")
@allure.tag("APIUsersService", "Positive")
@pytest.mark.PositiveApi
def test_create_user():
    response = ApiUsersService.create_api_user(credentials)
    assert_status_message(response, 200, 'User created')

@allure.title("Test change API user password")
@allure.description("This test attempt change password for last created user")
@allure.tag("APIUsersService", "Positive")
@pytest.mark.PositiveApi
def test_change_user_password():
    response = ApiUsersService.change_user_password()
    assert_status_message(response, 200, 'User password updated')

@allure.title("Test delete API user password")
@allure.description("This test attempt delete last created user")
@allure.tag("APIUsersService", "Positive")
@pytest.mark.PositiveApi
def test_delete_user():
    response = ApiUsersService.delete_api_user()
    assert_status_message(response, 200, 'User deleted')








import pytest

from data.users_credentials import credentials
from services.api_users_service import ApiUsersService
from services.utils import assert_status_message

@pytest.mark.PostiveApi
def test_create_user():
    response = ApiUsersService.create_api_user(credentials)
    assert_status_message(response, 200, 'User created')

@pytest.mark.PostiveApi
def test_change_user_password():
    response = ApiUsersService.change_user_password()
    assert_status_message(response, 200, 'User password updated')

@pytest.mark.PostiveApi
def test_delete_user():
    response = ApiUsersService.delete_api_user()
    assert_status_message(response, 200, 'User deleted')








import pytest

from data.users_credentials import credentials, existing_credentials
from services.api_users_service import ApiUsersService
from services.utils import assert_status_message


@pytest.mark.NegativeApi
def test_create_existing_user():
    response_existing = ApiUsersService.create_api_user(existing_credentials)

    message_existing = response_existing.json().get('message')
    assert_status_message(response_existing, 412, message_existing)

@pytest.mark.NegativeApi
def test_create_bad_request():
    response = ApiUsersService.create_bad_request()
    assert_status_message(response, 400, 'bad request data')
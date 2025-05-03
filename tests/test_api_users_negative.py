import pytest
import allure

from data.users_credentials import existing_credentials
from services.api_users_service import ApiUsersService
from services.utils import assert_status_message

@allure.title("Test create existing user")
@allure.description("This test attempt create user which was be created in positive group test")
@allure.tag("APIUsersService", "Negative")
@allure.id("create_existing_user")
@pytest.mark.NegativeApi
def test_create_existing_user():
    response_existing = ApiUsersService.create_api_user(existing_credentials)

    message_existing = response_existing.json().get('message')
    assert_status_message(response_existing, 412, message_existing)

@allure.title("Test create bad request")
@allure.description("This test create request with error data for bad request")
@allure.tag("APIUsersService", "Negative")
@allure.id("create_bad_request")
@pytest.mark.NegativeApi
def test_create_bad_request():
    response = ApiUsersService.create_bad_request()
    assert_status_message(response, 400, 'bad request data')
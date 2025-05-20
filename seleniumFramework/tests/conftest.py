import pytest
import logging
from selenium import webdriver

from helpers.cleanup import delete_user_by_login
from helpers.schemas.user_schema import CreateUserSchema, DeleteUserSchema
from seleniumFramework.pages.login_page import LoginPage
from services.api_users_service import ApiUsersService
from data.users_credentials import ui_user
from services.utils import validate_status_code_and_body

@pytest.fixture(scope="session", autouse=True)
def create_ui_user():
    response = ApiUsersService.create_api_user(ui_user)
    validate_status_code_and_body(response, CreateUserSchema, 200)

@pytest.fixture
def driver():
    driver = LoginPage(webdriver.Chrome())
    yield driver
    driver.quit_browser()

@pytest.fixture(scope="session", autouse=True)
def delete_ui_user():
    yield
    delete_user_by_login(ui_user)

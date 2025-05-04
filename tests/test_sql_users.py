import pytest
import allure

from data.db_users_data import LOGIN, EMAIL, NAME, PASSWORD
from services.db_service import DBService


@allure.title("Test create DB user")
@allure.description("This test attempt create new user in DB")
@allure.tag("DB_users", "Positive")
@allure.id("create_user")
@pytest.mark.sql
def test_create_user():
    DBService.create_user(LOGIN, EMAIL, NAME, PASSWORD)
    user = DBService.find_user_by_email(EMAIL)
    assert user is not None
    assert user[0] == LOGIN
    assert user[1] == EMAIL
    assert user[2] == NAME

@allure.title("Test find DB user")
@allure.description("This test attempt find new user in DB")
@allure.tag("DB_users", "Positive")
@allure.id("find_db_user")
@pytest.mark.sql
def test_find_user_by_email():
    user = DBService.find_user_by_email(EMAIL)
    assert user is not None
    assert user[2] == NAME

@allure.title("Test delete DB user")
@allure.description("This test attempt delete new user in DB")
@allure.tag("DB_users", "Positive")
@allure.id("delete_db_user")
@pytest.mark.sql
def test_delete_sql_user():
    DBService.delete_user_by_login(LOGIN)
    user = DBService.find_user_by_email(EMAIL)
    assert user is None
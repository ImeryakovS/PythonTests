from time import sleep

from seleniumFramework.data.settings import LOGIN, PASSWORD
from seleniumFramework.helpers.utils import check_element_exists
from seleniumFramework.pages.login_page import LoginPage


def test_successfully_login(driver):
    driver.enter_form(LoginPage.USERNAME_FIELD, LOGIN)
    driver.enter_form(LoginPage.PASSWORD_FIELD, PASSWORD)
    driver.click_button(LoginPage.LOGIN_BUTTON)
    check_element_exists(driver,'CSS_SELECTOR','[data-testid*="panel content"]')

def test_wrong_username_login(driver):
    driver.enter_form(LoginPage.USERNAME_FIELD, 'wrong_username')
    driver.enter_form(LoginPage.PASSWORD_FIELD, PASSWORD)
    driver.click_button(LoginPage.LOGIN_BUTTON, '[data-testid*="Alert"]' )
    check_element_exists(driver,'CSS_SELECTOR','[data-testid*="Alert"]')

def test_forgot_password(driver):
    driver.enter_form(LoginPage.USERNAME_FIELD, 'wrong_username')
    driver.enter_form(LoginPage.PASSWORD_FIELD, PASSWORD)
    driver.click_button(LoginPage.FORGOT_PASSWORD, LoginPage.FORGOT_FIELD )
    driver.enter_form(LoginPage.FORGOT_FIELD, 'LOGIN')
    check_element_exists(driver,'CSS_SELECTOR','[type="submit"]')

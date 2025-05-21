from time import sleep

from seleniumFramework.data.settings import LOGIN, PASSWORD
from seleniumFramework.helpers.utils import check_element_exists
from seleniumFramework.pages.login_page import LoginPage


def test_successfully_login(driver):
    driver.login(LOGIN, PASSWORD)
    driver.click_button_and_wait_next_selector(LoginPage.LOGIN_BUTTON)
    assert check_element_exists(driver,'CSS_SELECTOR','[data-testid*="panel content"]')

def test_wrong_username_login(driver):
    driver.login('wrong_username', PASSWORD)
    driver.click_button_and_wait_next_selector(LoginPage.LOGIN_BUTTON, '[data-testid*="Alert"]' )
    assert check_element_exists(driver,'CSS_SELECTOR','[data-testid*="Alert"]')

def test_forgot_password(driver):
    driver.login('wrong_username', PASSWORD)
    driver.click_button_and_wait_next_selector(LoginPage.FORGOT_PASSWORD, LoginPage.FORGOT_FIELD )
    driver.enter_form(LoginPage.FORGOT_FIELD, 'LOGIN')
    assert check_element_exists(driver,'CSS_SELECTOR','[type="submit"]')

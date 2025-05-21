from seleniumFramework.data.settings import LOGIN, PASSWORD
from seleniumFramework.helpers.utils import check_element_exists

def test_successfully_login(driver):
    driver.enter_username(LOGIN)
    driver.enter_password(PASSWORD)
    driver.click_login_button()
    check_element_exists(driver,'XPATH','//*[contains(@data-testid, "breadcrumb")]')

def test_wrong_username_login(driver):
    driver.enter_username('wrong_username')
    driver.enter_password(PASSWORD)
    driver.click_login_button()
    check_element_exists(driver,'CSS_SELECTOR','[data-testid*="Alert"]')

from seleniumFramework.data.settings import LOGIN, PASSWORD
from seleniumFramework.helpers.utils import check_element_exists

def test_base(driver):
    driver.go_to_login_page()
    driver.enter_username(LOGIN)
    driver.enter_password(PASSWORD)
    driver.click_login_button()
    check_element_exists(driver,'//*[contains(@data-testid, "breadcrumb")]')

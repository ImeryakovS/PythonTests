import logging

from selenium.webdriver.common.by import By
from seleniumFramework.data.settings import BASE_URL
from seleniumFramework.helpers.utils import wait_loading_page


class LoginPage:
    LOGIN_BUTTON = '[data-testid="data-testid Login button"]'
    USERNAME_FIELD = '[data-testid="data-testid Username input field"]'
    PASSWORD_FIELD = '[data-testid="data-testid Password input field"]'
    FORGOT_FIELD = '[name="userOrEmail"]'
    FORGOT_PASSWORD = 'a[href="/user/password/send-reset-email"]'

    def __init__(self, driver):
        logging.info(f"LoginPage hs received: {type(driver)}")
        self.driver = driver

    def go_to_login_page(self):
        self.driver.get(f'{BASE_URL}/login')
        logging.info(self.driver.current_url)

    def click_button(self, button, wait_selector=None):
        self.driver.find_element(By.CSS_SELECTOR, button).click()
        if wait_selector is not None:
            wait_loading_page(self.driver,wait_selector,)

    def enter_form(self, form, value):
        self.driver.find_element(By.CSS_SELECTOR, form).send_keys(value)

    def quit_browser(self):
        self.driver.quit()

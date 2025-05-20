import logging

from selenium.webdriver.common.by import By
from seleniumFramework.data.settings import BASE_URL

class LoginPage:
    LOGIN_BUTTON = '[data-testid="data-testid Login button"]'
    USERNAME_FIELD = '[data-testid="data-testid Username input field"]'
    PASSWORD_FIELD = '[data-testid="data-testid Password input field"]'

    def __init__(self, driver):
        self.driver = driver

    def go_to_login_page(self):
        self.driver.get(f'{BASE_URL}/login')
        logging.info(self.driver.current_url)

    def click_login_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.LOGIN_BUTTON).click()

    def enter_username(self, username):
        self.driver.find_element(By.CSS_SELECTOR, self.USERNAME_FIELD).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.CSS_SELECTOR, self.PASSWORD_FIELD).send_keys(password)

    def quit_browser(self):
        self.driver.quit()

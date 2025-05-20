from selenium.webdriver.common.by import By


class LoginPage:
    LOGIN_BUTTON = '[data-testid="data-testid Login button"]'
    USERNAME_FIELD = '[data-testid="data-testid Username input field"]'
    PASSWORD_FIELD = '[data-testid="data-testid Password input field"]'

    def __init__(self, driver):
        self.driver = driver

    def click_login_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.LOGIN_BUTTON).click()

    def enter_username(self, username):
        self.driver.find_element(By.CSS_SELECTOR, self.USERNAME_FIELD).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.CSS_SELECTOR, self.PASSWORD_FIELD).send_keys(password)

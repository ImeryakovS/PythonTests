import logging

from selenium import webdriver
from time import sleep

from seleniumFramework.helpers.utils import check_element_exists
from seleniumFramework.pages.login_page import LoginPage
from data.users_credentials import ui_user

driver = LoginPage(webdriver.Chrome())

def test_base():
    driver.go_to_login_page()
    driver.enter_username(ui_user['login'])
    driver.enter_password(ui_user['password'])
    driver.click_login_button()
    check_element_exists(driver,'//*[contains(@data-testid, "breadcrumb")]')
    sleep(5)
    driver.quit_browser()

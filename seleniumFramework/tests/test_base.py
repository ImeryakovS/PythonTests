import logging

from selenium import webdriver
from time import sleep

from seleniumFramework.pages.login_page import LoginPage

def test_base():
    driver = LoginPage(webdriver.Chrome())
    url = driver.go_to_login_page()
    logging.info(f'URL: {url}')
    username = driver.enter_username('test')
    password = driver.enter_password('<PASSWORD>')
    login = driver.click_login_button()
    sleep(2)
    driver.quit_browser()
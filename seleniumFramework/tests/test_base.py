import logging

from selenium import webdriver
from time import sleep
from seleniumFramework.data.settings import BASE_URL
from seleniumFramework.pages.login_page import LoginPage

def test_base():
    browser = webdriver.Chrome()
    logging.info(f'{BASE_URL}/login')
    browser.get(f'{BASE_URL}/login')
    username = LoginPage(browser).enter_username('test')
    password = LoginPage(browser).enter_password('<PASSWORD>')
    login = LoginPage(browser).click_login_button()
    sleep(2)
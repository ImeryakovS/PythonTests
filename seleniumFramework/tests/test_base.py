import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from seleniumFramework.data.settings import BASE_URL

browser = webdriver.Chrome()
logging.info(f'{BASE_URL}/login')
browser.get(f'{BASE_URL}/login')
click_login = browser.find_element(By.CSS_SELECTOR, '[data-testid="data-testid Login button"]')
click_login.click()

sleep(2)
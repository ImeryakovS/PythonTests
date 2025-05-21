import pytest
import logging

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def check_element_exists(page, selector_type,selector, timeout=10):
    if selector_type == 'XPATH':
        try:
            WebDriverWait(page.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, selector))
            )
            logging.info(f'Locator {selector} has been detected')
            return True
        except TimeoutException:
            pytest.fail(f'Timeout: Locator {selector} has not been detected')

    elif selector_type == 'CSS_SELECTOR':
        try:
            WebDriverWait(page.driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
            )
            logging.info(f'Locator {selector} has been detected')
            return True
        except TimeoutException:
            pytest.fail(f'Timeout: Locator {selector} has not been detected')
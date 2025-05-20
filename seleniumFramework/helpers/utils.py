import pytest
import logging

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def check_element_exists(page, xpath, timeout=10):
    try:
        WebDriverWait(page.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        logging.info(f'Locator {xpath} has been detected')
        return True
    except TimeoutException:
        pytest.fail(f'Timeout: Locator {xpath} has not been detected')
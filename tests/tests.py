import time

import pytest
from selenium.webdriver.common.by import By
from common.actions import Actions
from test_data import test_data as TD
def test_2(driver):
    driver.get(TD.base_url)
    time.sleep(6)


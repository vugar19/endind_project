import pytest
from common.actions import Actions
from test_data import test_data as TD
from utils.webdriver_instence_setup import webdriver_instance
@pytest.fixture()
def driver():
    driver = webdriver_instance()  # Replace with your desired webdriver
    yield driver
    driver.close()
    driver.quit()

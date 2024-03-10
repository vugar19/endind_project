import pytest
from utils.webdriver_instence_setup import webdriver_instance
@pytest.fixture()
def driver():
    driver = webdriver_instance()  # Replace with your desired webdriver
    yield driver
    driver.close()
    driver.quit()
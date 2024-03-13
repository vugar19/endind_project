import pytest
from common.actions import Actions
from test_data import test_data as TD
from time import sleep
from utils.webdriver_instence_setup import webdriver_instance

@pytest.fixture()
def driver():
    driver = webdriver_instance()
    yield driver
    driver.close()
    driver.quit()


# @pytest.fixture()
# def test_login(driver):
#     actions = Actions(driver)
#     driver.get(TD.base_url)
#
#     account = actions.find_element(TD.login_btn)
#     account.click()
#
#     phone = actions.find_element(TD.phone_number_input)
#     phone.click()
#     phone.send_keys(TD.oz_phone)
#
#     enter = actions.find_element(TD.enter_btn)
#     enter.click()
#
#     sleep(15)
#
#     enter_btn = actions.find_element(TD.enter_code_btn)
#     enter_btn.click()


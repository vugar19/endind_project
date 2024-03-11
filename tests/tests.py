import time

import pytest
from selenium.webdriver.common.by import By
from common.actions import Actions
from test_data import test_data as TD
def test_2(driver):
    actions = Actions(driver)
    driver.get(TD.base_url)
    time.sleep(184)
    account = actions.find_element(TD.login_btn)
    account.click()
    phone = actions.find_element(TD.phone_number_input)
    phone.click()
    phonenum = input('enter phone: ')
    phone.send_keys(phonenum)
    enter = actions.find_element(TD.enter_btn)
    enter.click()
    time.sleep(5)



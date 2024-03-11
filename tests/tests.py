import time
import pytest
from selenium.webdriver.common.by import By
from common.actions import Actions
from test_data import test_data as TD
def test_2(driver):
    actions = Actions(driver)
    driver.get(TD.base_url)

    account = actions.find_element(TD.login_btn)
    account.click()

    phone = actions.find_element(TD.phone_number_input)
    phone.send_keys(TD.oz_phone)

    enter = actions.find_element(TD.enter_btn)
    enter.click()



    time.sleep(5)

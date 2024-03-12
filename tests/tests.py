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
    phone.click()
    phone.send_keys(TD.oz_phone)

    enter = actions.find_element(TD.enter_btn)
    enter.click()

    code_box = actions.find_element(TD.enter_code_box)
    actions.send_keys(code_box,actions.input_text())
    time.sleep(15)

    something_btn = actions.find_element(TD.enter_code_btn)
    something_btn.click()

    assert driver.current_url == TD.base_url



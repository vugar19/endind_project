import time
import pytest
from selenium.webdriver.common.by import By
from common.actions import Actions
from test_data import test_data as TD


def test_delete_pending_tickets(driver):
    actions = Actions(driver)
    driver.get(TD.base_url)

    account = actions.find_element(TD.login_btn)
    account.click()

    phone = actions.find_element(TD.phone_number_input)
    phone.click()
    phone.send_keys(TD.noam_phone)

    enter = actions.find_element(TD.enter_btn)
    enter.click()

    time.sleep(30)

    something_btn = actions.find_element(TD.enter_code_btn)
    something_btn.click()

    # start ticket order here

    time.sleep(5)
    my_account_button = driver.find_element(By.XPATH, TD.my_account)
    my_account_button.click()

    time.sleep(5)
    tickets_button = driver.find_element(By.XPATH, TD.tickets)
    tickets_button.click()

    time.sleep(5)
    trash_ticket_button = driver.find_element(By.XPATH, TD.trash_ticket)
    trash_ticket_button.click()

    time.sleep(5)
    delete_button = driver.find_element(By.XPATH, TD.delete_confirmation_button)
    delete_button.click()

    time.sleep(3)
import time
import pytest
from selenium.webdriver.common.by import By
from common.actions import Actions
from test_data import test_data as TD


def test_delete_pending_tickets(driver):
    actions = Actions(driver)
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
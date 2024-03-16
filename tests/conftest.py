import pytest
from common.actions import Actions
from test_data import test_data as TD
import time
from selenium.webdriver.common.by import By
from utils.webdriver_instence_setup import webdriver_instance

@pytest.fixture()
def driver():
    driver = webdriver_instance()

    actions = Actions(driver)
    driver.get(TD.base_url)

    account = actions.find_element(TD.login_btn)
    account.click()

    phone = actions.find_element(TD.phone_number_input)
    phone.click()
    phone.send_keys(TD.phone)

    enter = actions.find_element(TD.enter_btn)
    enter.click()

    time.sleep(50)

    something_btn = actions.find_element(TD.enter_code_btn)
    something_btn.click()

    sport_options = actions.find_element(TD.first_cat)
    sport_options.click()
    time.sleep(3)

    event_links = driver.find_elements(By.XPATH, "//a[contains(@href, '/event/')]")
    processed_events = set()
    ticket_found = False
    for link in event_links:
        driver.implicitly_wait(5)
        event_number = link.get_attribute("href").split("/event/")[-1]
        driver.implicitly_wait(5)
        if event_number in processed_events:
            print(f"Event {event_number} has already been processed. Skipping...")
            continue
        link.click()
        time.sleep(3)
        try:
            purple_btn = driver.find_elements(By.XPATH, "//button[text()='לרכישה']")
            if purple_btn:
                ticket_found = True
                purple_btn[0].click()
                driver.implicitly_wait(4)
                break
            else:
                print('No available tickets for sale in this event')
                processed_events.add(event_number)
                driver.back()
                print(processed_events)
                driver.implicitly_wait(4)
        except StaleElementReferenceException:
            print('StaleElementReferenceException occurred. Retrying...')
            pass
    if not ticket_found:
        print('No tickets for sale in any event')

    yield driver
    driver.close()
    driver.quit()


import time
import pytest
from selenium.webdriver.common.by import By
from common.actions import Actions
from test_data import test_data as TD


@pytest.mark.parametrize("type_of_btn,result",[
    (TD.cancel_purchase_btn,TD.base_url),
    (TD.continue_purchase_btn,TD.payment_page_url)
])
def test_cancel_purchase(driver,type_of_btn,result):

    actions = Actions(driver)
    driver.get(TD.ticket_buying_page)

    main_cancel_btn = actions.find_element(TD.cancel_purchase_btn)
    main_cancel_btn.click()

    cancel_continue_btns = actions.find_element(type_of_btn)
    cancel_continue_btns.click()

    assert driver.current_url == result



@pytest.mark.skip
def test_for_loop2(driver):
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

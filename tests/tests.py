import time
import pytest
from selenium.webdriver.common.by import By
from common.actions import Actions
from test_data import test_data as TD


#
#
# def test_timer_func(driver):
#     actions = Actions(driver)
#     driver.get(TD.base_url)
#
#     event_ticket = actions.find_element(TD.event_ticket)
#     event_ticket.click()
#
#     buy_btn = actions.find_element(TD.buy_btn)
#     buy_btn.click()
#
#     pop_up_otp = actions.find_element(TD.pop_up_otp)
#     actions.input_text(pop_up_otp)
#
#     pop_up_otp_accept_btn = actions.find_element(TD.pop_up_otp_accept_btn)
#     pop_up_otp_accept_btn.click()
#
#     assert 'something' == 'something'
#
#
# def test_timer_expire_cancel(driver):
#     actions = Actions(driver)
#     driver.get(TD.base_url)
#
#     event_ticket = actions.find_element(TD.event_ticket)
#     event_ticket.click()
#
#     buy_btn = actions.find_element(TD.buy_btn)
#     buy_btn.click()
#
#     pop_up_otp = actions.find_element(TD.pop_up_otp)
#     actions.input_text(pop_up_otp)
#
#     pop_up_otp_accept_btn = actions.find_element(TD.pop_up_otp_accept_btn)
#     pop_up_otp_accept_btn.click()
#
#     cancel_purchase_btn = actions.find_element(TD.cancel_purchase_btn)
#     cancel_purchase_btn.click()
#
#     approve_cancel_purchase_btn = actions.find_element(TD.approve_cancel_purchase_btn)
#     approve_cancel_purchase_btn.click()
#
#     assert driver.current_url == TD.base_url
#
#
# def test_timer_expire_continue(driver):
#     actions = Actions(driver)
#     driver.get(TD.base_url)
#
#     event_ticket = actions.find_element(TD.event_ticket)
#     event_ticket.click()
#
#     buy_btn = actions.find_element(TD.buy_btn)
#     buy_btn.click()
#
#     pop_up_otp = actions.find_element(TD.pop_up_otp)
#     actions.input_text(pop_up_otp)
#
#     pop_up_otp_accept_btn = actions.find_element(TD.pop_up_otp_accept_btn)
#     pop_up_otp_accept_btn.click()
#
#     continue_purchase_btn = actions.find_element(TD.continue_purchase_btn)
#     continue_purchase_btn.click()
#
#     approve_continue_purchase_btn = actions.find_element(TD.approve_cancel_purchase_btn)
#     approve_continue_purchase_btn.click()
#
#     assert driver.current_url == driver.current_url
#
#
#
# @pytest.mark.parametrize('payment_option_path, inner_text',
#     ['//*[@a "google"]','google'],
#     ['//*[@a "paypal"]','paypal'],
#     ['//*[@a "apple pay"]','apple pay'],
#     ['//*[@a "credit"]','credit'])
# def test_payment_options(driver,payment_option_path,inner_text):
#     actions = Actions(driver)
#     driver.get(TD.base_url)
#
#     event_ticket = actions.find_element(TD.event_ticket)
#     event_ticket.click()
#
#     buy_btn = actions.find_element(TD.buy_btn)
#     buy_btn.click()
#
#     pop_up_otp = actions.find_element(TD.pop_up_otp)
#     actions.input_text(pop_up_otp)
#
#     pop_up_otp_accept_btn = actions.find_element(TD.pop_up_otp_accept_btn)
#     pop_up_otp_accept_btn.click()
#
#     payment_option = actions.find_element(payment_option_path)
#     payment_option_text = payment_option.get_attribute('innerText')
#     assert payment_option_text == inner_text


# def test_for_loop2(driver):
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
#     time.sleep(50)
#
#     something_btn = actions.find_element(TD.enter_code_btn)
#     something_btn.click()
#
#     sport_options = actions.find_element(TD.first_cat)
#     sport_options.click()
#     time.sleep(3)
#
#     ticket_found = False
#     location_links = driver.find_elements(By.XPATH, "//a[contains(@href, '/event/')]")
#     print(location_links)
    #
    # for link in location_links:
    #     link.click()
    #     time.sleep(3)
    #     purple_btn = driver.find_elements(By.XPATH, "//button[text()='לרכישה']")
    #     if purple_btn:
    #         ticket_found = True
    #         purple_btn[0].click()
    #         driver.implicitly_wait(4)
    #         break
    #     else:
    #         print('No available tickets for sale in this event')
    #         driver.back()
    #         time.sleep(3)
    #
    #
    # if not ticket_found:
    #     print('No tickets for sale in this category')

#
# def test_for_loop2(driver):
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
#     time.sleep(50)
#
#     something_btn = actions.find_element(TD.enter_code_btn)
#     something_btn.click()
#
#     sport_options = actions.find_element(TD.first_cat)
#     sport_options.click()
#     time.sleep(3)
#
#     processed_sessions = set()  # Set to track processed sessions
#
#     location_links = driver.find_elements(By.XPATH, "//a[contains(@href, '/event/')]")
#
#     for link in location_links:
#         session_id = link.get_attribute("id")  # Assuming ID is used to uniquely identify sessions
#         if session_id in processed_sessions:
#             print(f"Session {session_id} has already been processed. Skipping...")
#             continue
#
#         link.click()
#         time.sleep(3)
#         try:
#             purple_btn = driver.find_elements(By.XPATH, "//button[text()='לרכישה']")
#             if purple_btn:
#                 purple_btn[0].click()
#                 driver.implicitly_wait(4)
#                 break  # Exit loop after clicking button (adjust if needed)
#             else:
#                 print('No available tickets for sale in this event')
#         except StaleElementReferenceException:
#             print('StaleElementReferenceException occurred. Retrying...')
#             pass
#
#         # Mark session as processed
#         processed_sessions.add(session_id)
#
#         # Navigate back to the previous page
#         driver.back()
#         time.sleep(3)
#
#     if not ticket_found:
#         print('No tickets for sale in any event')
#



def test_for_loop2(driver):
    actions = Actions(driver)
    driver.get(TD.base_url)

    account = actions.find_element(TD.login_btn)
    account.click()

    phone = actions.find_element(TD.phone_number_input)
    phone.click()
    phone.send_keys(TD.oz_phone)

    enter = actions.find_element(TD.enter_btn)
    enter.click()

    time.sleep(50)

    something_btn = actions.find_element(TD.enter_code_btn)
    something_btn.click()

    sport_options = actions.find_element(TD.first_cat)
    sport_options.click()
    time.sleep(3)

    processed_events = set()  # Set to track processed events

    event_links = driver.find_elements(By.XPATH, "//a[contains(@href, '/event/')]")

    for link in event_links:
        event_number = link.get_attribute("href").split("/event/")[-1]  # Extract event number from URL
        if event_number in processed_events:
            print(f"Event {event_number} has already been processed. Skipping...")
            continue

        link.click()
        time.sleep(3)
        try:
            purple_btn = driver.find_elements(By.XPATH, "//button[text()='לרכישה']")
            if purple_btn:
                purple_btn[0].click()
                driver.implicitly_wait(4)
                break  # Exit loop after clicking button (adjust if needed)
            else:
                print('No available tickets for sale in this event')
        except StaleElementReferenceException:
            print('StaleElementReferenceException occurred. Retrying...')
            pass

        # Mark event as processed
        processed_events.add(event_number)

        # Navigate back to the previous page
        driver.back()
        time.sleep(3)

    if not ticket_found:
        print('No tickets for sale in any event')



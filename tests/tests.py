import time
import pytest
from selenium.webdriver.common.by import By
from common.actions import Actions
from test_data import test_data as TD
# @pytest.mark.skip
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
#     time.sleep(15)
#
#     something_btn = actions.find_element(TD.enter_code_btn)
#     something_btn.click()
#
#     assert driver.current_url == TD.base_url
#
# @pytest.mark.skip
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
# @pytest.mark.skip
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
# @pytest.mark.skip
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
# @pytest.mark.skip
# # @pytest.mark.parametrize('payment_option_path, inner_text',
# #     ['//*[@a "google"]','google'],
# #     ['//*[@a "paypal"]','paypal'],
# #     ['//*[@a "apple pay"]','apple pay'],
# #     ['//*[@a "credit"]','credit'])
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

    time.sleep(30)

    something_btn = actions.find_element(TD.enter_code_btn)
    something_btn.click()

    sport_options = actions.find_element(TD.first_cat)
    sport_options.click()


    location = actions.find_element(TD.location)
    location.click()
    time.sleep(5)

    event_link = actions.find_element(TD.event)
    event_link.click()
    time.sleep(5)

    purple_btns = driver.find_elements(By.TAG_NAME,'button')
    for btn in purple_btns:
        inner_btn = btn.get_attribute('innerText')
        if inner_btn == "לרכישה":
            time.sleep(10)
            btn.click()
            time.sleep(5)
            break
        else:
            print('no available ticket')







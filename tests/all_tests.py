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


def test_1(driver):
    action = Actions(driver)

    home = (By.XPATH,'//*[@id="root"]/div[1]/div/nav/div[1]/ul/a')
    home_btn = action.find_element(home)
    home_btn.click()
    sleep(10)

def test_2(driver):
    #valid test all fields filled correctly
    action = Actions(driver)

    card_number = (By.XPATH,'//*[@id="cardNumber"]')
    card_number_field= action.find_element(card_number)
    card_number_field.send_keys('4580439922377783')

    exp_month = (By.XPATH,'//*[@id="expmonth"]')
    exp_month_field = action.find_element(exp_month)
    exp_month_field.click()

    month_02 =(By.XPATH,'//*[@id="expmonth"]/option[3]')
    month_02_option = action.find_element(month_02)
    month_02_option.click()

    year= (By.XPATH,'//*[@id="expyear"]')
    year_field= action.find_element(year)
    year_field.click()

    year_number = (By.XPATH,'//*[@id="expyear"]/option[3]')
    year_number_2025= action.find_element(year_number)
    year_number_2025.click()

    cvv_code = (By.XPATH,'//*[@id="mycvv"]')
    cvv_number = action.find_element(cvv_code)
    cvv_number.send_keys(706)

    peyment = (By.XPATH,'//*[@id="submitbtn"]')
    click_peyment = action.find_element(peyment)
    click_peyment.click()

    assert ==

def test_3(driver):
        #invalid test credit card number with letters
        action = Actions(driver)

        card_number = (By.XPATH, '//*[@id="cardNumber"]')
        card_number_field = action.find_element(card_number)
        card_number_field.send_keys('45804q9922377783')
        error_massge_card_number = (By.XPATH,'//*[@id="payment_section_2"]/div[1]/div[2]')
        find_error_masssge_card_number = action.find_element(error_massge_card_number)
        validate_error_msg = find_error_masssge_card_number.get_attribute('innerText')
        expected = "Invalid Card Number"
        assert expected == validate_error_msg

def test_credit_card_number(driver):
    # invalid test credit card number with letters
    action = Actions(driver)
    cvv_number = (By.XPATH, '//*[@id="payment_section_2"]/div[3]/div[1]')
    cvv_number_field = action.find_element(cvv_number)
    cvv_number_field.send_keys('a12')
    error_massge_cvv_number = (By.XPATH, '//*[@id="payment_section_2"]/div[3]/div[2]')
    find_error_masssge_cvv_number= action.find_element(error_massge_cvv_number)
    validate_error_msg2 = find_error_masssge_cvv_number.get_attribute('innerText')
    expected = "Invalid CVV"
    assert expected == validate_error_msg2

def test_5(driver):
    action = Actions(driver)
    card_number_desc = (By.XPATH, '//*[@id="cardNumber"]')
    find_card_number_desc = action.find_element(card_number_desc)
    validate_card_desc = find_card_number_desc.get_attribute('place holder')
    expected ="Card Number"
    assert expected == validate_card_desc


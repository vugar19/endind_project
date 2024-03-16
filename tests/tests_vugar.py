from common.actions import Actions
from selenium.webdriver.common.by import By
from time import sleep
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

    def test_4(driver):
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








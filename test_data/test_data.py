from selenium.webdriver.common.by import By

base_url = 'https://portal-dev.safsarglobal.link/'
login_btn = (By.XPATH,'//a[contains(text(),"התחברות")]')
phone_number_input = (By.XPATH,'//*[@id="root"]/main/div/div[2]/div/form/input')
enter_btn = (By.XPATH,'//*[@id="root"]/main/div/div[2]/div/form/button')

oz_phone = '0525232330'

enter_code_box = (By.XPATH,'//body/div[@id="root"]/main[1]/div[1]/div[2]/div[1]/form[1]/input[1]')

enter_code_btn = (By.XPATH,"//body/div[@id='root']/main[1]/div[1]/div[2]/div[1]/form[1]/button[1]")


event_ticket = "d"
buy_btn = "ws"
pop_up_otp = "s"
pop_up_otp_accept_btn = 'ssk'
cancel_purchase_btn = 'aaaa'
approve_cancel_purchase_btn = "aa"
approve_continue_purchase_btn = "aa"
continue_purchase_btn = "ff"
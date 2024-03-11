from selenium.webdriver.common.by import By

base_url = 'https://portal-dev.safsarglobal.link/'
login_btn = (By.XPATH,'//a[contains(text(),"התחברות")]')
phone_number_input = (By.XPATH,'//*[@id="root"]/main/div/div[2]/div/form/input')
enter_btn = (By.XPATH,'//*[@id="root"]/main/div/div[2]/div/form/button')

oz_phone = '0525232330'

enter_code_box = '//body/div[@id="root"]/main[1]/div[1]/div[2]/div[1]/form[1]/input[1]'

enter_code_btn = "//body/div[@id='root']/main[1]/div[1]/div[2]/div[1]/form[1]/button[1]"

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

categories = (By.XPATH,"//body/div[@id='root']/main[1]/div[2]/div[2]/div[1]/div[1]/div[2]/a[5]")
location = (By.XPATH,"//div[@id='rc-tabs-0-tab-tab4']")

purple_btn = (By.XPATH,"//*[contains(@class, 'px-8 py-2 bg-primaryPurple text-white text)]")

first_cat = (By.XPATH,'//body/div[@id="root"]/div[2]/div[2]/div[1]/div[1]/div[2]/a[3]')
event_tickets = "//*[contains(@class, 'hidden md:grid grid-cols-1 md:grid-cols-5 text-[18px] my-4')]"

logo =  (By.XPATH,"//*[@class='hidden md:flex space-x-10 md:w-[500px]']")
picture = (By.XPATH,'//body/div[@id="root"]/main[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[4]/a[1]/div[1]/img[1]')
# all_locations = driver.find_elements(By.XPATH,'//*[@class="py-4"]')
# for event in all_locations:
#     event.click()
#     event_tickets = driver.find_elements(By.XPATH,TD.event_ticket)
#     for ticket in event_tickets:
#         purple_btn = actions.find_element(TD.purple_btn)
#         innertext = purple_btn.get_attribute('innerText')
#         if innertext == "לרכישה":
#             purple_btn.click()
#             time.sleep(10)
#             break
#         else:
#             logo = actions.find_element(TD.logo)
#             logo.click()
#             time.sleep(10)
#
#
#

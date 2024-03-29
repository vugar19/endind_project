from selenium.webdriver.common.by import By

base_url = 'https://portal-dev.safsarglobal.link/'
login_btn = (By.XPATH,'//a[contains(text(),"התחברות")]')
phone_number_input = (By.XPATH,'//*[@id="root"]/main/div/div[2]/div/form/input')
enter_btn = (By.XPATH,'//*[@id="root"]/main/div/div[2]/div/form/button')

phone = '0552603210'
ticket_buying_page = 'https://portal-dev.safsarglobal.link/order-summary/148/confirmation/9541943373'

enter_code_box = (By.XPATH,'//body/div[@id="root"]/main[1]/div[1]/div[2]/div[1]/form[1]/input[1]')

enter_code_btn = (By.XPATH,"//body/div[@id='root']/main[1]/div[1]/div[2]/div[1]/form[1]/button[1]")

payment_page_url = 'https://portal-dev.safsarglobal.link/order-summary/180/payment/3143889120'

ticket_caneling_main_btn = (By.XPATH,'//*[@id="root"]/main/div[2]/div[2]/div/div/div[1]/p[1]/span')
buy_btn = "ws"

cancel_purchase_btn = (By.XPATH,'//*[@id="root"]/main/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/button[2]')

continue_purchase_btn = (By.XPATH,'//*[@id="root"]/main/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/button[1]')

categories = (By.XPATH,"//body/div[@id='root']/main[1]/div[2]/div[2]/div[1]/div[1]/div[2]/a[5]")
location = (By.XPATH,"//div[@id='rc-tabs-0-tab-tab4']")

purple_btn = (By.XPATH,"//*[contains(@class, 'px-8 py-2 bg-primaryPurple text-white text)]")

first_cat = (By.XPATH,'//*[@href="/category-search-results/1/ספורט"]')
event_tickets = "//*[contains(@class, 'hidden md:grid grid-cols-1 md:grid-cols-5 text-[18px] my-4')]"

event = (By.XPATH, '//body/div[@id="root"]/main[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[4]/a[1]/div[1]/img[1]')

logo =  (By.XPATH,"//*[@class='hidden md:flex space-x-10 md:w-[500px]']")
picture = (By.CLASS_NAME,'py-4')


noam_phone = '0502320277'
my_account = '//*[@id="root"]/div[1]/div/nav/div[1]/ul/button'
tickets = '//*[@id="root"]/main/div[2]/div[1]/div[3]/div/div[1]/div[1]/div/div[2]'
trash_ticket = ''
delete_confirmation_button = ''
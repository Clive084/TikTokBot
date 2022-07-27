from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
PATH="C:/Users/clive/Downloads/chromedriver.exe"
r=list()
user="orang3_"
xchecking=[]
#passs=input('Password:')
#(hint) usual password but with a capital at the start
driver=webdriver.Chrome(PATH)
driver.get("https://quackr.io/temporary-phone-number-generator")
while True:
    try:
        driver.find_element(By.XPATH,'//*[@id="wrapper"]/div[1]/main/app-temporary-phone-number-generator/section/div/div[1]/div/div/div[1]/button').click()
        break
    except Exception as e:
        print(e)
while True:
    try:
        driver.find_element(By.XPATH,'//*[@id="wrapper"]/div[1]/main/app-temporary-phone-number-generator/section/div/div[1]/div/div/div[2]/div/a[24]').click()
        break
    except:
        pass
driver.find_element(By.XPATH,'//*[@id="wrapper"]/div[1]/main/app-temporary-phone-number-generator/section/div/div[1]/div/div/button').click()
while True:
    try:
        driver.find_element(By.XPATH,'//*[@id="wrapper"]/div[1]/main/messages/section/div/div/div/h1/i').click()
        break
    except:
        pass
phone_number=driver.find_element(By.XPATH,'//*[@id="wrapper"]/div[1]/main/messages/section/div/div/div/h1').text
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://www.tiktok.com/signup/phone-or-email/phone")
while True:
    try:
        driver.find_element(By.XPATH,'//*[@id="loginContainer"]/div[1]/form/div[3]/div[1]').click()
        break
    except:
        pass
driver.find_element(By.XPATH,'//*[@id="loginContainer"]/div[1]/form/div[3]/div[1]/div[2]/div[3]').click()
driver.find_element(By.XPATH,'//*[@id="loginContainer"]/div[1]/form/div[3]/div[2]/div[1]').click()
driver.find_element(By.XPATH,'//*[@id="loginContainer"]/div[1]/form/div[3]/div[2]/div[2]/div[7]').click()
driver.find_element(By.XPATH,'//*[@id="loginContainer"]/div[1]/form/div[3]/div[3]/div[1]').click()
driver.find_element(By.XPATH,'//*[@id="loginContainer"]/div[1]/form/div[3]/div[3]/div[2]/div[23]').click()
driver.find_element(By.XPATH,'//*[@id="loginContainer"]/div[1]/form/div[6]/div/div[1]/div').click()
driver.find_element(By.XPATH,'//*[@id="loginContainer"]/div[1]/form/div[6]/div/div[1]/div[2]/div[1]/input').send_keys("uk")
driver.find_element(By.XPATH,'//*[@id="U"]/li[2]/span').click()
driver.find_element(By.XPATH,'//*[@id="loginContainer"]/div[1]/form/div[6]/div/div[2]/input').send_keys(phone_number[3:])
driver.find_element(By.XPATH,'//*[@id="loginContainer"]/div[1]/form/div[7]/div/button').click()
time.sleep(3)
try:
    if driver.find_element(By.XPATH,'//*[@id="loginContainer"]/div[1]/form/div[6]/div[2]'):
        print("dfdwadafwagawgawggsdfghjljkhgghhgfhgfgfdsfsdfadswqewqrewtretreyreutrut")
except:
    try:
        if driver.find_element(By.XPATH,'//*[@id="captcha_container"]/div/div[1]/div[2]/div'):
            while True:
                try:
                    driver.find_element(By.XPATH,'//*[@id="captcha_container"]/div/div[1]/div[2]/div')
                except:
                    break
    except:
        pass
driver.switch_to.window(driver.window_handles[0])

input()

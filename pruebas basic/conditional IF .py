import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

driver=webdriver.Chrome(executable_path="C:\DRIVES\chromedriver.exe")

driver.get("https://www.seleniumeasy.com/")
driver.maximize_window()
t = 3
#condicional IF

titulo=driver.find_element_by_xpath("//img[@src='https://www.seleniumeasy.com/sites/all/themes/seasy/logo.png']")

print(titulo.is_displayed())

btn1=driver.find_element_by_xpath("//h2[contains(.,'Selenium Python')]")
btn2=driver.find_element_by_xpath("//a[@title='python tutorials']")

if (titulo.is_displayed()==True):
     print("Existe la imagen")
     btn1.click()
     time.sleep(t)
     btn2.click()
else:
    print("No existe la imagen")

time.sleep(t)
driver.close()
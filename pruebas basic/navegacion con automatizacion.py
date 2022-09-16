import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By



t=0.010
driver=webdriver.Chrome(executable_path="C:\DRIVES\chromedriver.exe")

#driver=webdriver.Firefox(executable_path="C:\DRIVES\geckodriver.exe")

driver.get("https://testingqarvn.com.es/")
driver.maximize_window()
time.sleep(t)

driver.get("https://qastack.mx/")
time.sleep(t)

driver.get("https://www.codegrepper.com/")
time.sleep(t)

driver.execute_script("window.history.go(-1)")
time.sleep(t)

driver.execute_script("window.history.go(2)")
time.sleep(t)
#driver.forward()
driver.execute_script("window.history.go(-1)")
time.sleep(t)
driver.close()
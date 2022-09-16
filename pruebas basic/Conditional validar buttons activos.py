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
#condicional validar bottons

btn1=driver.find_element_by_xpath("//img[@src='https://www.seleniumeasy.com/sites/all/themes/seasy/logo.png']")
print(btn1.is_enabled())

if (btn1.is_enabled()== True):
    print("Puedes dar click")
else:
    print("No puedes dar click")


time.sleep(t)
driver.close()
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

driver=webdriver.Chrome(executable_path="C://DRIVES//chromedriver.exe")
driver.get("https://demo.seleniumeasy.com/basic-checkbox-demo.html")
driver.maximize_window()
driver.implicitly_wait(10)
t=4

btn1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@type,'checkbox')])[1]")))
btn1.click()

btn3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@type,'checkbox')])[3]")))
btn3.click()

btn2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@type,'checkbox')])[2]")))
btn2.click()

btn4 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@type,'checkbox')])[4]")))
btn4.click()

driver.execute_script("window.scrollTo(0,300)")

time.sleep(t)
driver.close()
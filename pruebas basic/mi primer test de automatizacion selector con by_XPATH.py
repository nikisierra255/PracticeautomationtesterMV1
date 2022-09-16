import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\DRIVES\chromedriver.exe")

#driver=webdriver.Firefox(executable_path="C:\DRIVES\geckodriver.exe")

driver.get("https://testingqarvn.com.es/datos-personales/")
driver.maximize_window()
time.sleep(1)

nombre = driver.find_element(By.XPATH,"//input[contains(@id,'wsf-1-field-21')]")
nombre.send_keys("Nikito")
time.sleep(1)
driver.find_element_by_xpath("//input[contains(@id,'wsf-1-field-22')]").send_keys("Sierra")
time.sleep(1)
driver.find_element_by_xpath("//input[contains(@id,'wsf-1-field-23')]").send_keys("nikisierra255@gmail.com")
time.sleep(1)
driver.find_element_by_xpath("//input[contains(@id,'wsf-1-field-24')]").send_keys("8095474885")
time.sleep(1)
driver.find_element_by_xpath("//textarea[contains(@id,'wsf-1-field-28')]").send_keys("direccion del mar, santo domingo")
time.sleep(1)
driver.execute_script("window.scrollTo(0,500)")
time.sleep(2)
driver.find_element(By.XPATH,"//button[contains(@id,'wsf-1-field-27')]").click()
time.sleep(3)

driver.close()
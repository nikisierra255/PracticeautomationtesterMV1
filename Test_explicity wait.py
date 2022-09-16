import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\DRIVES\chromedriver.exe")
driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
driver.maximize_window()
driver.implicitly_wait(10)
t=0.23

element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='at-cv-lightbox-button-holder']/a[2]")))
element.click()

driver.find_element_by_xpath("//input[contains(@id,'user-message')]").send_keys("Bienvenido a Selenium" + Keys.TAB + Keys.ENTER)
time.sleep(t)

driver.find_element_by_xpath("//input[contains(@id,'sum1')]").send_keys("5"+Keys.TAB + "5" + Keys.TAB + Keys.ENTER)
time.sleep(t)



time.sleep(t)
driver.close()
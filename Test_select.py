import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="C:\DRIVES\chromedriver.exe")
driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
driver.maximize_window()
driver.implicitly_wait(10)
t=0.32

#dias = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='at-cv-lightbox-button-holder']/a[2]")))
diaSelect=driver.find_element_by_xpath("//select[contains(@id,'select-demo')]")

ds=Select(diaSelect)

ds.select_by_visible_text("Sunday")
time.sleep(t)

ds.select_by_index("2")
time.sleep(t)

ds.select_by_value("Tuesday")

ciudad=Select(driver.find_element_by_id("multi-select"))

ciudad.select_by_index(1)
time.sleep(t)

ciudad.select_by_index(4)
time.sleep(t)

ciudad.select_by_index(6)
time.sleep(t)


time.sleep(t)
driver.close(t)
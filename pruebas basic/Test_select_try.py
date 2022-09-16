import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
driver.maximize_window()
driver.implicitly_wait(10)
t=.7
driver=webdriver.Chrome(executable_path="C:\DRIVES\chromedriver.exe")


try:
 #diaSelect = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//select[contains(@id,'select-demo1')]")))
 diaSelect = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//select[contains(@id,'select-demo')]")))

 dias=Select(diaSelect)
 dias.select_by_visible_text("Sunday")
 time.sleep(t)
 dias.select_by_index("2")
 time.sleep(t)
 dias.select_by_value("Tuesday")
 time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print("Elemento no disponible")


 #segundo bloque
ciudad=Select(driver.find_element_by_id("multi-select"))

ciudad.select_by_index(1)
time.sleep(t)

ciudad.select_by_index(4)
time.sleep(t)

ciudad.select_by_index(6)
time.sleep(t)


time.sleep(t)
driver.close()
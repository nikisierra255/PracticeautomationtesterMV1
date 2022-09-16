import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

driver=webdriver.Chrome(executable_path="C:\DRIVES\chromedriver.exe")
driver.get("https://pixabay.com/es/")
driver.maximize_window()
driver.implicitly_wait(10)
t=2

#driver.execute_script("window.scrollTo(0,1500)")


try:
 #buscar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id,'fileinput')]1')]")))
 buscar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//label[contains(.,'Descubre más')]")))
 buscar = driver.find_element_by_xpath("//label[contains(.,'Descubre más')]")
 ir=driver.execute_script("arguments[0].scrollIntoView();" ,buscar)
 time.sleep(t)
except TimeoutException as ex:
    print(ex.msg)
    print("Elemento no disponible")


time.sleep(t)
driver.close()
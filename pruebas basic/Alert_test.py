import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

driver=webdriver.Chrome(executable_path="C:\DRIVES\chromedriver.exe")

driver.get("https://demo.seleniumeasy.com/bootstrap-modal-demo.html")
driver.maximize_window()
t = 2

#driver.find_element_by_xpath("//a[@href='#myModal0']").click()

#driver.switch_to_alert().accept() #segun la documentacion le dara al boton aceptar.

#driver.switch_to_alert().dismiss() # segun la documentacion esto debe de jalar, pero no lo hace


#driver.find_element_by_xpath("(//a[@href='#'][contains(.,'Save changes')])[1]").click()
#time.sleep(t)

driver.find_element_by_xpath("//a[@href='#myModal0']").click()
time.sleep(t)

try:
    buscar=WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//a[@href='#'][contains(.,'Save changes')])[1]")))
    buscar=driver.find_element_by_xpath("(//a[@href='#'][contains(.,'Save changes')])[1]").click()
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")

#driver.find_element_by_xpath("(//a[@href='#'][contains(.,'Close')])[1]").click()

time.sleep(t)
driver.close()
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\DRIVES\chromedriver.exe")

#driver=webdriver.Firefox(executable_path="C:\DRIVES\geckodriver.exe")

driver.get("https://testingqarvn.com.es/datos-personales/")
driver.maximize_window()
driver.implicitly_wait(0.10) #nos da un tiempo para esperar un elemento que falte en la pagina

t=2
time.sleep(t)

nombre = driver.find_element_by_xpath("//input[contains(@id,'wsf-1-field-21')]") #para ver en accion el implicity wait, quitar  el (ID) de xpath
nombre.send_keys("Nikito")
time.sleep(t)
driver.find_element_by_xpath("//input[contains(@id,'wsf-1-field-22')]").send_keys("Sierra")
time.sleep(t)
driver.find_element_by_xpath("//input[contains(@id,'wsf-1-field-23')]").send_keys("nikisierra255@gmail.com")
time.sleep(t)
driver.find_element_by_xpath("//input[contains(@id,'wsf-1-field-24')]").send_keys("8095474885")
time.sleep(t)
driver.find_element_by_xpath("//textarea[contains(@id,'wsf-1-field-28')]").send_keys("direccion del mar, santo domingo")
time.sleep(t)
driver.execute_script("window.scrollTo(0,300)")
time.sleep(t)
driver.find_element_by_xpath("//button[contains(@id,'wsf-1-field-27')]").click()
time.sleep(t)

driver.close()
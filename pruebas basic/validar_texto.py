import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

driver=webdriver.Chrome(executable_path="C:\DRIVES\chromedriver.exe")

driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()
t = 3

btnEnviar=driver.find_element_by_xpath("//button[@type='submit'][contains(.,'Send')]")
btnEnviar.click()
time.sleep(t)

name_val=driver.find_element_by_xpath("//small[@class='help-block'][contains(.,'Please supply your first name')]")
name=name_val.text

#print("El valor de error es: "+name)
if (name =="Please supply your first name" ):
   #print("Falta el nombre")
   campoNombre=driver.find_element_by_xpath("//input[contains(@name,'first_name')]")
   campoNombre.send_keys("Nikito")
   time.sleep(t)
   print("Nombre correcto")
else:
    #print("Nombre correcto")
    print("Falta el nombre")



apellido_val=driver.find_element_by_xpath("//small[@class='help-block'][contains(.,'Please supply your last name')]")
apellido=apellido_val.text

#print("El valor de error es: "+name)
if (apellido =="Please supply your last name" ):
   #print("Falta el nombre")
   campoApellido=driver.find_element_by_xpath("//input[contains(@name,'last_name')]")
   campoApellido.send_keys("Sierra")
   time.sleep(t)
   print("Apellido correcto")
else:
    #print("Nombre correcto")
    print("Falta el apellido")

print(btnEnviar.is_enabled())

if (btnEnviar.is_enabled() == False):
    print("Faltan campos por llenar")

else:
    print("Todo es Ok")
time.sleep(t)
driver.close()
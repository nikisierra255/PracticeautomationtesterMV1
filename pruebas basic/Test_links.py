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
t = 2

#obteniendo todos los links de una pagina

links=driver.find_elements(By.TAG_NAME, "a")

print("El numero de Links que hay en la pagina es: ",len(links))

for num in links:
    print(num.text)

driver.find_element_by_link_text("Date pickers").click()
time.sleep(t)

driver.find_element_by_link_text("JQuery Date Picker").click()

time.sleep(t)
driver.close()
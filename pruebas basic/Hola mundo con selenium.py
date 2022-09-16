from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver=webdriver.Chrome(executable_path="C:\DRIVES\chromedriver.exe")

driver=webdriver.Firefox(executable_path="C:\DRIVES\geckodriver.exe")

driver.get("https://www.fuprocom.org/contacto/")

print("Bienvenido al hola mundo con selenium")

print(driver.title)

driver.close()
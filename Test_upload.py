import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

driver=webdriver.Chrome(executable_path="C:\DRIVES\chromedriver.exe")
driver.get("https://testpages.herokuapp.com/styled/file-upload-test.html")
driver.maximize_window()
driver.implicitly_wait(10)
t=2


try:
 #buscar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id,'fileinput')]1')]")))
 buscar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id,'fileinput')]")))
 buscar = driver.find_element_by_xpath("//input[contains(@id,'fileinput')]")
 buscar.send_keys("C://Users//carlos manuel//PycharmProjects//curso selenium//Imagenes//demo1.jpg")
 time.sleep(t)
 driver.find_element_by_xpath("//input[contains(@id,'itsanimage')]").click()
 driver.find_element_by_xpath("//input[contains(@type,'submit')]").click()
 time.sleep(t)


except TimeoutException as ex:
    print(ex.msg)
    print("Elemento no disponible")


time.sleep(t)
driver.close()
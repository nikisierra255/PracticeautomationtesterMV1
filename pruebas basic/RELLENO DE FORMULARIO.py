import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

driver = webdriver . Chrome(executable_path="C:\DRIVES\chromedriver.exe")

driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()
t = 2

try:
 driver . find_element_by_xpath("//input[contains(@name,'first_name')]").send_keys("Nikito")
 time .sleep(t)
 driver .find_element_by_xpath("//input[contains(@name,'last_name')]").send_keys("Sierra")
 time .sleep(t)
 driver .execute_script("window.scrollTo(0,200)")
 driver .find_element_by_xpath("//input[contains(@name,'email')]").send_keys("nikisierra255@gmail.com")
 time .sleep(t)
 driver .find_element_by_xpath("//input[contains(@name,'phone')]").send_keys("8095474885")
 time .sleep(t)
 driver .find_element_by_xpath("//input[contains(@name,'address')]").send_keys("avenida nicolas de ovando")
 time .sleep(t)
 driver .find_element_by_xpath("//input[contains(@name,'city')]").send_keys("santo domingo")
 time .sleep(t)
 ciudad = Select(driver.find_element_by_xpath("//select[contains(@name,'state')]"))

 ciudad .select_by_index(5)
 driver .find_element_by_xpath("//input[contains(@name,'zip')]").send_keys("10501")
 time .sleep(t)
 driver .find_element_by_xpath("//input[contains(@name,'website')]").send_keys("www.fuprocom.com")
 time .sleep(t)
 driver .find_element_by_xpath("//input[contains(@value,'yes')]").click()
 time .sleep(t)
 driver .find_element_by_xpath("//textarea[contains(@class,'form-control')]").send_keys("Practica de slenium with python")
 time .sleep(t)
 driver .find_element_by_xpath("//button[@type='submit'][contains(.,'Send')]").click()

except TimeoutException as ex:
    print(ex.msg)
    print(" Elemento no disponible ")

time .sleep(5)
driver .close()
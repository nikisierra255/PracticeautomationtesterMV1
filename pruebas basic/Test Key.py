import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\DRIVES\chromedriver.exe")

#driver=webdriver.Firefox(executable_path="C:\DRIVES\geckodriver.exe")

driver.get("https://testingqarvn.com.es/datos-personales/")
driver.maximize_window()
time.sleep(1)

driver.execute_script("window.scrollTo(0,500)")

nombre = driver.find_element_by_xpath("//input[@type='text' or @id='class=wsf-label' or @id='wsf-1-field-23']")
nombre.send_keys("Nikito")
nombre.send_keys(Keys.TAB + "sierra" + Keys.TAB + "NIKISIERRA255@GMAIL.COM" + Keys.TAB + "829-886-2346" +
                 Keys.TAB + "santo domingo, cristo rey" + Keys.TAB)
driver.find_element_by_xpath("//button[contains(@id,'wsf-1-field-27')]").click()
time.sleep(3)

driver.find_element_by_xpath("(//a[@href='https://testingqarvn.com.es/'][contains(.,'Inicio')])[1]").click()

driver.execute_script("window.scrollTo(0,800)")

driver.find_element_by_xpath("//img[contains(@width,'750')]").click()
time.sleep(1)
driver.execute_script("window.scrollTo(0,400)")
time.sleep(1)
driver.find_element_by_xpath("//a[@class='et_pb_button et_pb_button_0 et_pb_bg_layout_light'][contains(.,'Ir al Curso completo')]").click()
time.sleep(1)
time.sleep(1)

driver.close()
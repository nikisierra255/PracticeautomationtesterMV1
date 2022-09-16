import time


import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException



class PruebaLogin(unittest.TestCase):


    def  setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\DRIVES\chromedriver.exe")
        # driver=webdriver.Chrome(executable_path="C:\DRIVES\chromedriver.exe")
        time.sleep(4)

    def test_login1(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        nom=driver.find_element_by_xpath("//input[contains(@id,'user-name')]")
        clave=driver.find_element_by_xpath("//input[contains(@id,'password')]")
        boton=driver.find_element_by_xpath("//input[contains(@id,'login-button')]")
        nom.send_keys("Nikito")
        clave.send_keys("adm123456@")
        boton.click()
        error=driver.find_element_by_xpath("//h3[contains(@data-test,'error')]")
        error=error.text
        #print(error)
        if (error == "Epic sadface: Username and password do not match any user in this service"):
            print("El error de los datos es correcto")
            print("Prueba Uno Pass")
        time.sleep(4)

    def test_login2(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        nom=driver.find_element_by_xpath("//input[contains(@id,'user-name')]")
        clave=driver.find_element_by_xpath("//input[contains(@id,'password')]")
        boton=driver.find_element_by_xpath("//input[contains(@id,'login-button')]")
        nom.send_keys("")
        clave.send_keys("adm123456@")
        boton.click()
        error=driver.find_element_by_xpath("//h3[contains(@data-test,'error')]")
        error=error.text
        #print(error)

        if (error == "Epic sadface: Username is required"):
            print("Falta el nombre")
            print("Prueba Dos Pass")

        time.sleep(4)


    def test_login3(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        nom=driver.find_element_by_xpath("//input[contains(@id,'user-name')]")
        clave=driver.find_element_by_xpath("//input[contains(@id,'password')]")
        boton=driver.find_element_by_xpath("//input[contains(@id,'login-button')]")
        nom.send_keys("Nikito")
        clave.send_keys("")
        boton.click()
        error=driver.find_element_by_xpath("//h3[contains(@data-test,'error')]")
        error=error.text
        #print(error)

        if (error == "Epic sadface: Password is required"):
            print("Falta la Clave")
            print("Prueba Tres Pass")

        time.sleep(4)


    def test_login4(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        nom=driver.find_element_by_xpath("//input[contains(@id,'user-name')]")
        clave=driver.find_element_by_xpath("//input[contains(@id,'password')]")
        boton=driver.find_element_by_xpath("//input[contains(@id,'login-button')]")
        nom.send_keys("")
        clave.send_keys("")
        boton.click()
        error=driver.find_element_by_xpath("//h3[contains(@data-test,'error')]")
        error=error.text
        #print(error)

        if (error == "Epic sadface: Username is required"):
            print("Faltan las credenciales")
            print("Prueba cuatro issue")

        time.sleep(4)



    def test_login5(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        nom=driver.find_element_by_xpath("//input[contains(@id,'user-name')]")
        clave=driver.find_element_by_xpath("//input[contains(@id,'password')]")
        boton=driver.find_element_by_xpath("//input[contains(@id,'login-button')]")
        nom.send_keys("standard_user")
        clave.send_keys("secret_sauce")
        boton.click()

        Elemento=driver.find_element_by_xpath("//div[contains(@class,'app_logo')]")
        Elemento.is_displayed()
        print("El elemento es: "+str(Elemento))
        print("Prueba Cinco Pass")

        time.sleep(4)

    def tearDown(self):
        driver = self.driver
        driver.close()
        time.sleep(4)

if __name__ == "__main__":
    unittest.main()


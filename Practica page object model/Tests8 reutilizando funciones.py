import time


import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from FuncionesPropias.FuncionesGlobales1 import Funciones1
from FuncionesPropias.pagina_login import page_login

t=7

class Base_Test(unittest.TestCase):


    def  setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\DRIVES\chromedriver.exe")
        # driver=webdriver.Chrome(executable_path="C:\DRIVES\chromedriver.exe")
        time.sleep(1)

    def test1(self):
        driver = self.driver
        f = Funciones1(driver)
        pg=page_login(driver)
        pg.Login_Master("https://www.saucedemo.com/","Nikito","Hola",t)
        print("Validado con exito")



    def tearDown(self):
        driver = self.driver
        driver.close()
        time.sleep(2)

if __name__ == "__main__":
    unittest.main()

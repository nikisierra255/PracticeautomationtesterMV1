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


class Base_Test(unittest.TestCase):


    def  setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\DRIVES\chromedriver.exe")
        # driver=webdriver.Chrome(executable_path="C:\DRIVES\chromedriver.exe")
        time.sleep(4)

    def test1(self):
        driver = self.driver
        f = Funciones1(driver)
        f.Navegar("https://www.saucedemo.com/",2)
        f.Texto_ID("user-name","nikito",2)
        f.Texto_ID("password","hola123456",2)


    def tearDown(self):
        driver = self.driver
        driver.close()
        time.sleep(2)

if __name__ == "__main__":
    unittest.main()

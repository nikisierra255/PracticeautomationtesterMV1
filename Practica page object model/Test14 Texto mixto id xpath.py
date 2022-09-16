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

t=5
class Base_Test(unittest.TestCase):


    def  setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\DRIVES\chromedriver.exe")
        # driver=webdriver.Chrome(executable_path="C:\DRIVES\chromedriver.exe")
        time.sleep(4)

    def test1(self):
        driver = self.driver
        f = Funciones1(driver)
        f.Navegar("https://testingqarvn.com.es/datos-personales/",5)
        f.Texto_mixto("id","wsf-1-field-21","nikito",t)
        f.Texto_mixto("id","wsf-1-field-22", "sierra",t)
        f.Texto_mixto("id","wsf-1-field-23","nikisierra@gmail.com",t)
        f.Texto_mixto("id","wsf-1-field-24","829-886-2346",t)
        f.Texto_mixto("id","wsf-1-field-28","calle primera",t)
        f.Click_mixto("id","wsf-1-field-27",t)


    def tearDown(self):
        driver = self.driver
        driver.close()
        time.sleep(4)

if __name__ == "__main__":
    unittest.main()


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
        f.Navegar("https://demo.seleniumeasy.com/basic-checkbox-demo.html",5)
        for n in range(2,6):
            f.Check_Xpath_Multiples(3,"(//input[contains(@type,'checkbox')])["+str(n)+"]")


    def tearDown(self):
        driver = self.driver
        driver.close()
        time.sleep(4)

if __name__ == "__main__":
    unittest.main()


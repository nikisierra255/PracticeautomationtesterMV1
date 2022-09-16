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

t=2

class Base_Test(unittest.TestCase):


    def  setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\DRIVES\chromedriver.exe")
        # driver=webdriver.Chrome(executable_path="C:\DRIVES\chromedriver.exe")
        time.sleep(1)

    def test1(self):
        driver = self.driver
        f = Funciones1(driver)
        f.Navegar("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html",t)
        #f.Select_Xpath_Text("//select[contains(@id,'select-demo')]","Sunday",t)
        #f.Select_Xpath_Type("//select[contains(@id,'select-demo')]","text","Monday",t)
        #f.Select_Xpath_Type("//select[contains(@id,'select-demo')]", "value", "Saturday", t)
        #f.Select_Xpath_Type("//select[contains(@id,'select-demo')]", "index", "4", t)
        f.Select_ID_Type("select-demo","index","5",t)




    def tearDown(self):
        driver = self.driver
        driver.close()
        time.sleep(t)

if __name__ == "__main__":
    unittest.main()
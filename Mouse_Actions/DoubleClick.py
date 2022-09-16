import time

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from ..FuncionesPropias.FuncionesGlobales1 import Funciones1
from selenium.webdriver import ActionChains

t = 5
class Base_Test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C://DRIVES//chromedriver.exe")
        # driver = webdriver.Chrome(executable_path="C://DRIVES//chromedriver.exe")


    def test1(self):
        driver = self.driver
        f = Funciones1(driver)
        f.Navegar("https://demoqa.com/buttons",t)




        Elemento = driver.find_element(By.ID,"doubleClickBtn")
        act = ActionChains(driver)
        act.double_click(Elemento).perform()


        time.sleep(5)





    def tearDown(self):
        driver = self.driver
        driver.close()
        time.sleep(4)

if __name__ == "__main__":
    unittest.main()

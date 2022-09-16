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

t=3
class Base_Test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C://DRIVES//chromedriver.exe")
        # driver = webdriver.Chrome(executable_path="C://DRIVES//chromedriver.exe")


    def test1(self):
        driver = self.driver
        f = Funciones1(driver)
        f.Navegar("https://jqueryui.com/droppable/",t)

        f.Mouse_dragAnDdrop_ActionChair("xpath","//div[contains(@id,'draggable')]", 150,130,3)

    def tearDown(self):
        driver = self.driver
        driver.close()
        time.sleep(4)

if __name__ == "__main__":
    unittest.main()

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

    '''''
    def test1(self):
        driver = self.driver
        f = Funciones1(driver)
        f.Navegar("https://jqueryui.com/droppable/",t)

        f.Click_ActionChair_x_y("xpath","//a[@href='https://jqueryui.com/demos/'][contains(.,'Demos')]", 200,0,)
    '''''

    def test1(self):
        driver = self.driver
        f = Funciones1( driver )
        f.Navegar( "https://www.google.com/webhp?hl=es&sa=X&ved=0ahUKEwjAnaD69tP2AhUrQzABHeQACGoQPAgI", t )

        f.Texto_mixto("xpath","(//input[contains(@aria-label,'Buscar')])[1]", "ferr",4)

        f.Click_ActionChair_x_y( "xpath", "(//input[contains(@aria-label,'Buscar')])[1]",0,150,5)










    def tearDown(self):
        driver = self.driver
        driver.close()
        time.sleep(4)

if __name__ == "__main__":
    unittest.main()

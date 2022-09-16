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
        f = Funciones1( driver )
        f.Navegar( "https://demoqa.com/automation-practice-form", t )

        f.Texto_mixto("xpath","//input[contains(@id,'firstName')]","Nikito",2)


        f.Copiar_y_pegar(driver)

        '''''
        act = ActionChains(driver)
        act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        time.sleep(2)
        act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
        act.send_keys(Keys.TAB)
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        time.sleep(2)
        act.send_keys(Keys.TAB)
        act.key_down( Keys.CONTROL ).send_keys( "v" ).key_up( Keys.CONTROL ).perform()
        '''



    def tearDown(self):
        driver = self.driver
        driver.close()
        time.sleep(4)

if __name__ == "__main__":
    unittest.main()

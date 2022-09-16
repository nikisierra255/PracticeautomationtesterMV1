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
        f.Navegar("https://opensource-demo.orangehrmlive.com/",t)
        f.Texto_mixto("id","txtUsername","Admin",t)
        f.Texto_mixto("id","txtPassword","admin123",t)
        f.Click_mixto("id","btnLogin",t)


        Admin =driver.find_element(By.ID,"menu_admin_viewAdminModule")
        sub1 = driver.find_element(By.ID,"menu_admin_UserManagement")
        sub2 = driver.find_element(By.ID,"menu_admin_viewSystemUsers")


        act = ActionChains(driver)
        act.move_to_element(Admin).move_to_element(sub1).move_to_element(sub2).click().perform()





    def tearDown(self):
        driver = self.driver
        driver.close()
        time.sleep(4)

if __name__ == "__main__":
    unittest.main()

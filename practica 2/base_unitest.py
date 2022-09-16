import time


import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException



class base_test(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome(executable_path="C:\DRIVES\chromedriver.exe")
        self.driver.maximize_window()
        #driver=webdriver.Chrome(executable_path="C:\DRIVES\chromedriver.exe")
        time.sleep(20)

    def tes1(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        time.sleep(20)

    def tearDown(self):
        driver = self.driver
        driver.close()
        time.sleep(20)

if __name__=='__main__':
    unittest.main()


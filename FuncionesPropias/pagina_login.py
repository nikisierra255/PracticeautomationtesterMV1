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

t=2

class page_login():

    def __init__(self , driver):
        self.driver = driver

    def Login_Master(self,url,name,clave,t):
        driver = self.driver
        f = Funciones1(driver)
        f.Navegar(url, t)
        f.Texto_Xpath_Validar("//input[contains(@id,'user-name')]", name, t)
        f.Texto_Xpath_Validar("//input[contains(@id,'password')]", clave, t)
        f.Click_Xpath_Validar("//input[contains(@id,'login-button')]", t)
        f.salida()

import time
import unittest
from Funciones_Excel import *

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from FuncionesPropias.FuncionesGlobales1 import Funciones1

t=3
class Base_Test(unittest.TestCase):


    def  setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\DRIVES\chromedriver.exe")
        # driver=webdriver.Chrome(executable_path="C:\DRIVES\chromedriver.exe")
        time.sleep(4)

    def test1(self):
        driver = self.driver
        f = Funciones1(driver)
        fe=FuncionesExcel(driver)
        f.Navegar("https://demoqa.com/text-box",t)
        ruta = "C://Users//carlos manuel//Desktop//CURSO QA TESTER RECURSOS//datos.xlsx"
        filas=fe.getRowCount(ruta,"Hoja1")

        for r in range(2,filas+1):
            Nombre=fe.readData(ruta,"Hoja1",r,1)
            Email=fe.readData(ruta,"Hoja1",r,2)
            Direccion=fe.readData(ruta,"Hoja1",r,3)
            Direccion1=fe.readData(ruta,"Hoja1",r,4)

            f.Texto_mixto( "id", "userName", Nombre, t )
            f.Texto_mixto( "id", "userEmail", Email, t )
            f.Texto_mixto( "id", "currentAddress", Direccion, t )
            f.Texto_mixto( "id", "permanentAddress", Direccion1, t )
            f.Click_mixto( "id", "submit", t )

            e=f.Existe("id","name",t)
            if (e=="Existe"):
                print ("El elemento  se inserto correctamente")
                fe.writeData(ruta,"Hoja1",r,5,"Insertado")
            else:
                print ("No se inserto")
                fe.writeData(ruta,"Hoja1",r,5,"Error")




    def tearDown(self):
        driver = self.driver
        driver.close()
        time.sleep(4)

if __name__ == "__main__":
    unittest.main()


import time


import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains


class Funciones1():

    def __init__(self, driver):
        self.driver=driver


    def saludos(self):
        print("Bienevenido a Page Object Model")




    def Tiempo(self,tie):
        t=time.sleep(tie)
        return t



    def Navegar(self,Url,Tiempo):
        self.driver.get(Url)
        print("pagina abierta: "+str(Url))
        self.driver.maximize_window()
        t=time.sleep(Tiempo)
        return t



    def Texto_Xpath(self,xpath,texto,Tiempo):
        val=self.driver.find_element_by_xpath(xpath)
        val.clear()
        val.send_keys(texto)
        print( "Escribiendo en el campo:----> {} el texto:---> {}".format( xpath, texto ) )
        t=time.sleep(Tiempo)
        return t



    def Texto_ID(self,ID,texto,Tiempo):
        val=self.driver.find_element_by_id(ID)
        val.clear()
        val.send_keys(texto)
        print( "Escribiendo en el campo:---> {} el texto:---> {}".format( ID, texto ) )
        t=time.sleep(Tiempo)
        return t


#mejorando nuestra funcion xpath

    def Texto_Xpath_Validar(self,xpath,texto,Tiempo):
        try:
            val =  WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
            val =  self.driver.find_element_by_xpath(xpath)
            val.clear()
            val.send_keys(texto)
            print("Escribiendo en el campo:---> {} el texto:---> {}".format(xpath,texto))
            t = time.sleep(Tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento" + xpath)


#mejorando nuestra funcion ID

    def Texto_ID_Validar(self,ID,texto,Tiempo):
        try:
            val =  WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,id)))
            val = self.driver.execute_script( "arguments[0].scrollIntoView();", val )
            val =  self.driver.find_element_by_id(id)
            val.clear()
            val.send_keys(texto)
            print( "Escribiendo en el campo: --> {} el texto: --->{}".format( ID, texto ) )
            t = time.sleep(Tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el Elemento" + id)

#Funcion dar click a un elemento con xpath

    def Click_Xpath_Validar(self, xpath, Tiempo):
        try:
            val = WebDriverWait( self.driver, 5 ).until( EC.visibility_of_element_located(( (By.XPATH, xpath) ) ))
            val = self.driver.execute_script( "arguments[0].scrollIntoView();", val )
            val = self.driver.find_element_by_xpath( xpath )
            val.click()
            print( "Dando Click en el campo:----> {}".format( xpath) )
            t = time.sleep( Tiempo )
            return t
        except TimeoutException as ex:
            print( ex.msg )
            print( "No se encontro el Elemento" + xpath )


#Funcion dar click a un elemento con ID

    def Click_ID_Validar(self, id, Tiempo):
        try:
            val = WebDriverWait( self.driver, 5 ).until( EC.visibility_of_element_located(( (By.ID, id) ) ))
            val = self.driver.execute_script( "arguments[0].scrollIntoView();", val )
            val = self.driver.find_element_by_id( id )
            val.click()
            print( "Dando Click en el campo:-----> {}".format(id) )
            t = time.sleep( Tiempo )
            return t
        except TimeoutException as ex:
            print( ex.msg )
            print( "No se encontro el Elemento" + id )


    def Salida(self):
        print("Se termina la prueba Exitosamente")



#Funcion para validar CheckBox con Xpath

    def Select_Xpath_Text(self, xpath,text, Tiempo):
        try:
            val = WebDriverWait( self.driver, 5 ).until( EC.visibility_of_element_located(( (By.XPATH, xpath) ) ))
            val = self.driver.execute_script( "arguments[0].scrollIntoView();", val )
            val = self.driver.find_element_by_xpath( xpath )
            val=Select(val)
            val.select_by_visible_text(text)
            print( "El campo selecionado es:----> {}".format( text) )
            t = time.sleep( Tiempo )
            return t
        except TimeoutException as ex:
            print( ex.msg )
            print( "No se encontro el Elemento" + xpath )


#Funcion para validar CheckBox con Xpath mediante Text, Index y Value

    def Select_Xpath_Type(self, xpath,tipo,dato, Tiempo):
        try:
            val = WebDriverWait( self.driver, 5 ).until( EC.visibility_of_element_located(( (By.XPATH, xpath) ) ))
            val = self.driver.execute_script( "arguments[0].scrollIntoView();", val )
            val = self.driver.find_element_by_xpath( xpath )
            val=Select(val)
            if (tipo == "text"):
                val.select_by_visible_text(dato)
            elif(tipo == "index"):
                val.select_by_index(dato)
            elif(tipo == "value"):
                val.select_by_value(dato)
            print( "El campo selecionado es:-----> {}".format(dato) )
            t = time.sleep( Tiempo )
            return t
        except TimeoutException as ex:
            print( ex.msg )
            print( "No se encontro el Elemento" + xpath )


#Funcion para validar CheckBox con ID mediante Text, Index y Value

    def Select_ID_Type(self, id,tipo,dato, Tiempo):
        try:
            val = WebDriverWait( self.driver, 5 ).until( EC.visibility_of_element_located(( (By.ID, id) ) ))
            val = self.driver.execute_script( "arguments[0].scrollIntoView();", val )
            val = self.driver.find_element_by_id( id )
            val=Select(val)
            if (tipo == "text"):
                val.select_by_visible_text(dato)
            elif(tipo == "index"):
                val.select_by_index(dato)
            elif(tipo == "value"):
                val.select_by_value(dato)
            print( "El campo selecionado es:-----> {}".format(dato) )
            t = time.sleep( Tiempo )
            return t
        except TimeoutException as ex:
            print( ex.msg )
            print( "No se encontro el Elemento" + id )




#Funcion para cargar un archivo a una pagina mediante un Xpath

    def Upload_Xpath(self,xpath,ruta, Tiempo):
        try:
            val = WebDriverWait( self.driver, 5 ).until( EC.visibility_of_element_located(( (By.XPATH, xpath) ) ))
            val = self.driver.execute_script( "arguments[0].scrollIntoView();", val )
            val = self.driver.find_element_by_xpath( xpath )
            val.send_keys(ruta)
            print( "Se esta cargando el archivo:-----> {}".format(ruta) )
            t = time.sleep( Tiempo )
            return t
        except TimeoutException as ex:
            print( ex.msg )
            print( "No se encontro el Elemento" + xpath )



#Funcion para cargar un archivo a una pagina mediante un ID

    def Upload_ID(self,id,ruta, Tiempo):
        try:
            val = WebDriverWait( self.driver, 5 ).until( EC.visibility_of_element_located(( (By.ID, id) ) ))
            val = self.driver.execute_script( "arguments[0].scrollIntoView();", val )
            val = self.driver.find_element_by_id( id )
            val.send_keys(ruta)
            print( "Se esta cargando el archivo:-----> {}".format(ruta) )
            t = time.sleep( Tiempo )
            return t
        except TimeoutException as ex:
            print( ex.msg )
            print( "No se encontro el Elemento" + id )


#Funcion para hacer radio y Check PO xpath

    def Check_Xpath(self,xpath, Tiempo):
        try:
            val = WebDriverWait( self.driver, 5 ).until( EC.visibility_of_element_located(( (By.XPATH, xpath) ) ))
            val = self.driver.execute_script( "arguments[0].scrollIntoView();", val )
            val = self.driver.find_element_by_xpath( xpath )
            val.click()
            print( "Dando Click en el Elemento:-----> {}".format(xpath) )
            t = time.sleep( Tiempo )
            return t
        except TimeoutException as ex:
            print( ex.msg )
            print( "No se encontro el Elemento" + xpath )

#Funcion para hacer radio y Check PO id

    def Check_ID(self,id, Tiempo):
        try:
            val = WebDriverWait( self.driver, 5 ).until( EC.visibility_of_element_located(( (By.ID, id) ) ))
            val = self.driver.execute_script( "arguments[0].scrollIntoView();", val )
            val = self.driver.find_element_by_id( id )
            val.click()
            print( "Dando Click en el Elemento:-----> {}".format(id) )
            t = time.sleep( Tiempo )
            return t
        except TimeoutException as ex:
            print( ex.msg )
            print( "No se encontro el Elemento" + id )


#Funcion para hacer radio y Check PO xpath multiples seleccion

    def Check_Xpath_Multiples(self,Tiempo,*args):
        try:
            for num in args:
                val = WebDriverWait( self.driver, 5 ).until( EC.visibility_of_element_located(( (By.XPATH, num) ) ))
                val = self.driver.execute_script( "arguments[0].scrollIntoView();", val )
                val = self.driver.find_element_by_xpath( num )
                val.click()
                print( "Dando Click en el Elemento:-----> {}".format(num) )
                t = time.sleep( Tiempo )
            return t
        except TimeoutException as ex:
            for num in args:
                print( ex.msg )
                print( "No se encontro el Elemento" + num )



    def SEXP_ID(self,elemento):
        val = WebDriverWait( self.driver, 5 ).until( EC.visibility_of_element_located( (By.ID, elemento) ) )
        val = self.driver.execute_script( "arguments[0].scrollIntoView();", val )
        val = self.driver.find_element(By.ID, elemento )
        return val

    def SEXP_XPATH(self, elemento):
        val = WebDriverWait( self.driver, 5 ).until( EC.visibility_of_element_located( (By.XPATH, elemento) ) )
        val = self.driver.execute_script( "arguments[0].scrollIntoView();", val )
        val = self.driver.find_element(By.XPATH, elemento )
        return val



#mejorando nuestra funcion texto mixto xpath/Id

    def Texto_mixto(self,tipo,selector,texto,Tiempo):
        if(tipo =="xpath"):
           try:
               val=self.SEXP_XPATH(selector)
               val.clear()
               val.send_keys(texto)
               print("Escribiendo en el campo:---> {} el texto:---> {}".format(selector,texto))
               t = time.sleep(Tiempo)
               return t
           except TimeoutException as ex:
               print(ex.msg)
               print("No se encontro el Elemento" + selector)

        elif (tipo == "id"):
            try:
                val = self.SEXP_ID(selector)
                val.clear()
                val.send_keys( texto )
                print( "Escribiendo en el campo:---> {} el texto:---> {}".format( selector, texto ) )
                t = time.sleep( Tiempo )
                return t
            except TimeoutException as ex:
                print( ex.msg )
                print( "No se encontro el Elemento" + selector )




#Funcion dar click a un elemento mixto entre xpath y Id

    def Click_mixto(self, tipo, selector,tiempo):
        if (tipo == "xpath"):
            try:
                val=self.SEXP_XPATH(selector)
                val.click()
                print( "Dando Click en el Elemento:---> {}".format( selector,selector) )
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print( ex.msg )
                print( "No se encontro el Elemento" + selector )

        elif (tipo == "id"):
            try:
                val = self.SEXP_ID( selector )
                val.click()
                print( "Dando click en ele elemento:---> {}".format( selector,selector) )
                t = time.sleep( tiempo )
                return t
            except TimeoutException as ex:
                print( ex.msg )
                print( "No se encontro el Elemento" + selector )




#Funcion existe para el sistema de datadriver

    def Existe(self,tipo,selector,Tiempo):
        if(tipo =="xpath"):
           try:
               val =  WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,selector)))
               val = self.driver.execute_script("arguments[0].scrollIntoView();",val)
               val =  self.driver.find_element_by_xpath(selector)

               print("El elemento: {}---> Existe ".format(selector))
               t = time.sleep(Tiempo)
               return "Existe"
           except TimeoutException as ex:
               print(ex.msg)
               print("No se encontro el Elemento" + selector)
               return "No existe"

        elif (tipo == "id"):
            try:
                val = WebDriverWait( self.driver, 5 ).until( EC.visibility_of_element_located( (By.ID, selector) ) )
                val = self.driver.execute_script( "arguments[0].scrollIntoView();", val )
                val = self.driver.find_element_by_id( selector )
                print("El elemento: {}---> Existe ".format( selector ))
                t = time.sleep( Tiempo )
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return "No existe"



#Funcion dar click a un elemento mixto entre xpath y Id funcion ActionChains

    def Mousedoubleclick_mixto_ActionChair(self, tipo, selector,tiempo=2):
        if (tipo == "xpath"):
            try:
                val = WebDriverWait( self.driver, 5 ).until( EC.visibility_of_element_located( (By.XPATH,selector) ) )
                val = self.driver.execute_script( "arguments[0].scrollIntoView();", val )
                val = self.driver.find_element_by_xpath( selector )
                act = ActionChains(self.driver)
                act.double_click(val).perform()
                print( "Dando DoubleClick en el Elemento:---> {}".format( selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print( ex.msg )
                print( "No se encontro el Elemento" + selector )

        elif (tipo == "id"):
            try:
                val = WebDriverWait( self.driver, 5 ).until( EC.visibility_of_element_located( (By.ID, selector)))
                val = self.driver.execute_script( "arguments[0].scrollIntoView();", val )
                val = self.driver.find_element_by_id( selector )
                act = ActionChains( self.driver )
                act.double_click( val ).perform()
                print( "Dando DoubleClick en el Elemento:---> {}".format( selector))
                t = time.sleep( tiempo )
                return t
            except TimeoutException as ex:
                print( ex.msg )
                print( "No se encontro el Elemento" + selector )




#Funcion dar click derecho a un elemento mixto entre xpath y Id funcion ActionChains

    def Mouse_Buttons_derecho_ActionChair(self, tipo, selector,tiempo=2):
        if (tipo == "xpath"):
            try:
                val = self.SEXP_XPATH(selector)
                act = ActionChains(self.driver)
                act.context_click(val).perform()
                print( "Dando Click Derecho en el Elemento:---> {}".format( selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print( ex.msg )
                print( "No se encontro el Elemento" + selector )

        elif (tipo == "id"):
            try:
                val = self.SEXP_ID(selector)
                act = ActionChains( self.driver )
                act.context_click(val).perform()
                print( "Dando Click Derecho en el Elemento:---> {}".format( selector))
                t = time.sleep( tiempo )
                return t
            except TimeoutException as ex:
                print( ex.msg )
                print( "No se encontro el Elemento" + selector )





#Funcion para arastrar y sortar un elemento mixto entre xpath y Id funcion ActionChains

    def Mouse_dragAnDdrop_ActionChair_arrastrar_y_soltar(self, tipo, selector1,destino,tiempo=2):
        if (tipo == "xpath"):
            try:
                val = self.SEXP_XPATH(selector1)
                val2= self.SEXP_XPATH(destino)
                act = ActionChains(self.driver)
                act.drag_and_drop(val,val2).perform()
                print( "Arrastrando y Soltando el Elemento:---> {}".format(selector1))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print( ex.msg )
                print( "No se encontro el Elemento" + selector1)

        elif (tipo == "id"):
            try:
                val = self.SEXP_ID(selector1)
                val2 = self.SEXP_ID(destino)
                act = ActionChains( self.driver )
                act.drag_and_drop(val,val2).perform()
                print("Arrastrando y Soltando el Elemento:---> {}".format(selector1))
                t = time.sleep( tiempo )
                return t
            except TimeoutException as ex:
                print( ex.msg )
                print( "No se encontro el Elemento" + selector1)



#Funcion para arastrar y sortar un elemento mixto entre xpath y Id funcion ActionChains MEDIANTE COORDENADA(X,Y)

    def Mouse_dragAnDdrop_ActionChair_x_y(self, tipo, selector1,X,Y,tiempo=2):
        if (tipo == "xpath"):
            try:
                self.driver.switch_to.frame(0)
                val = self.SEXP_XPATH(selector1)
                act = ActionChains(self.driver)
                act.drag_and_drop_by_offset(val,X,Y).perform()
                print( "Arrastrando y Soltando el Elemento:---> {}".format(selector1))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print( ex.msg )
                print( "No se encontro el Elemento" + selector1)

        elif (tipo == "id"):
            try:
                self.driver.switch_to.frame(0)
                val = self.SEXP_ID(selector1)
                act = ActionChains( self.driver )
                act.drag_and_drop_by_offset(val,X,Y).perform()
                print("Arrastrando y Soltando el Elemento:---> {}".format(selector1))
                t = time.sleep( tiempo )
                return t
            except TimeoutException as ex:
                print( ex.msg )
                print( "No se encontro el Elemento" + selector1)



#Funcion para dar Click en un elemento mixto entre xpath y Id funcion ActionChains MEDIANTE COORDENADA(X,Y)

    def  Click_ActionChair_x_y(self, tipo, selector1,X,Y,tiempo=2):
        if (tipo == "xpath"):
            try:
                #self.driver.switch_to.frame(0)
                val = self.SEXP_XPATH(selector1)
                act = ActionChains(self.driver)
                act.move_to_element_with_offset(val,X,Y).click().perform()
                print( "Dando Click en el elemento {} , coordenada {} , {}".format(selector1, X,Y))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print( ex.msg )
                print( "No se encontro el Elemento" + selector1)

        elif (tipo == "id"):
            try:
                #self.driver.switch_to.frame(0)
                val = self.SEXP_ID(selector1)
                act = ActionChains( self.driver )
                act.move_to_element_with_offset( val, X, Y ).click().perform()
                print( "Dando Click en el elemento {} , coordenada {} , {}".format( selector1, X, Y ) )
                t = time.sleep( tiempo )
                return t
            except TimeoutException as ex:
                print( ex.msg )
                print( "No se encontro el Elemento" + selector1)








#Funcion para Copiar y Pegar en un elemento mixto entre xpath y Id funcion ActionChains

    def  Copiar_y_pegar(self,driver):
        act = ActionChains( driver )
        act.key_down( Keys.CONTROL ).send_keys( "a" ).key_up( Keys.CONTROL ).perform()
        time.sleep( 2 )
        act.key_down( Keys.CONTROL ).send_keys( "c" ).key_up( Keys.CONTROL ).perform()
        act.send_keys( Keys.TAB )
        act.key_down( Keys.CONTROL ).send_keys( "v" ).key_up( Keys.CONTROL ).perform()
        time.sleep( 2 )
        act.send_keys( Keys.TAB )
        act.key_down( Keys.CONTROL ).send_keys( "v" ).key_up( Keys.CONTROL ).perform()





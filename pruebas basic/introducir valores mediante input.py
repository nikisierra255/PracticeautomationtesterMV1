print ("cual es tu nombre:  ")
nom=input()

print ("cual es tu primer apellido:  ")
apellidopaterno = input()

print ("cual es tu segundo apellido:  ")
apellidomaterno = input()

print ("introduzca el valor de (a):  ")
a = input()
a = int(a)  #ojo se debe de convertir el valor de a para que la suma se pueda realizar
print ("introduzca el valor de (b):  ")
b = input()
b = int(b)  # de igual manera se debe de realizar la convercion de b a int para que la suma de los dos numeros se puedan realizar
suma = a + b

print(" tu nombre completo es:  {} {} {}".format(nom, apellidopaterno,apellidomaterno))
print(" la suma de {} + {} = {}".format(a,b,suma))

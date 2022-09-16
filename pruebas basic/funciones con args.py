def suma(*args):
    resultado = 0
    for n in args:
        resultado = resultado + n
    print("el resultado es: "+str(resultado))

suma(5,9)
#crear una lista en python
lenguajes = ["php","python","sql","c#","java","html5"]
print(lenguajes)
print("lenguaje seleccionado: "+lenguajes[0])
#cambiar un elemnto de la lista por el remplazable
lenguajes[2]="Nodejs"

print("lenguajes "+lenguajes[2])
#agregar un elemnto mas a la lista
lenguajes.append("ruby")

print(lenguajes)
#eliminar un elemento de la lista
lenguajes.remove("c#")
print(lenguajes)
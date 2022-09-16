a = 65
b = 50
c = 8

print ("es a igual b: " + str(b==a))
print("es a menor que b: " + str(a<b))
print("es a mayor que b: "+ str(a>b))
print("es a menor o igual que b: "+ str(b<=a))
print("es a mayor o igual que b: " +str(a>=b))
print("es a diferente que b: " +str(b!=a))


#concatenacion con operadores logicos and
print("si a es menor de b y a es menor que c: "+str(a<b and a<c))
print("si a es menor de b y a es menor que c: "+str(b<a and c<a))

#concatenacion con operadores logicos or

print ("si a es menor que b o c es mayor que a: " +str(a<b) or (c>a))
print ("si b es mayor que a o a es menor que c: " +str(b>a) or (a<c))
#s1={1,2,3,4,5}
#s2={4,5}

x = 5
y = 2

S1 = set()
print ("Debera Ingresar", x, "numeros para el 1er conjunto de datos")

for i in range(x):
    print("Ingrese el valor", i+1)
    S1.add(int(input("Numero: ")))
    print("\n")

S2 = set()
print ("Debera Ingresar", y, "numeros para el 2do conjunto de datos")

for i in range(y):
    print("Ingrese el valor", i+1)
    S2.add(int(input("Numero: ")))
    print("\n")


print("Los valores ingresados del 1er conjunto de datos son:", S1)
print("Los valores ingresados del 2do conjunto de datos son:", S2)

if S2.issubset(S1):
   print ("S2 es un subconjunto de S1")
else:
   print ("S2 no es un subconjunto de S1")

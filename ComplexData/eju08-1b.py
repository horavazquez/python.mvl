x = 5

print ("Debera Ingresar", x, "numeros")
#T1 = (6, 7, 8, 9, 1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2)
L1 = []
# Utilizo una lista pues las tuplas son inmutables y no tienen metodos para actualizarlas
for i in range(x):
    print("Ingrese el valor", i+1)
    L1.append(int(input("Numero: ")))
    print("\n")
# Convierto la lista en tupla
T1 = tuple(L1)
T2 = ()
for x in T1:
   if x not in T2:
      T2+=(x,)
print ("La tupla original es:", T1)
print("Los valores ingresados sin repetir son:", T2)

x = 5
print ("Debera Ingresar", x, "numeros")
#L1 = [3, 5, 9, 1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2, 8]
L1 = []
for i in range(x):
    print("Ingrese el valor", i+1)
    L1.append(int(input("Numero: ")))
    print("\n")

L2 = []
for x in L1:
   if x not in L2:
      L2.append(x)

print ("La Lista original es:", L1)      
print("Los valores ingresados sin repetir son:", L2)


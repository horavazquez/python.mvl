import random
L1 = []
elementos = 10
for i in range(elementos):
   x = random.randint(0, 100)
   L1.append(x)

print ("El listado aleatorio de numeros es:", L1)
print("\n")

ttl = 0
for x in L1:
   ttl+=x
print ("La Suma de los elementos Usando un ciclo for es:", ttl)

ttl = sum(L1)
print ("La Suma de los elementos Usando la funcion sum() es:", ttl)
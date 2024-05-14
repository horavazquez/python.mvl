import random
S1 = set()
elementos = 10

for i in range(elementos):
   x = random.randint(0, 100)
   S1.add(x)

print ("El listado aleatorio de numeros es:", S1)
print("\n")

ttl = 0
for x in S1:
   ttl+=x
print ("La Suma de los elementos Usando un ciclo for es:", ttl)

ttl = sum(S1)
print ("La Suma de los elementos Usando la funcion sum() es:", ttl)
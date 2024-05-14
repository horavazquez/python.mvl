import random
T1 = ()
elementos = 10

for i in range(elementos):
   x = random.randint(0, 100)
   T1+=(x,)

print ("El listado aleatorio de numeros es:", T1)
print("\n")

ttl = 0
for x in T1:
   ttl+=x
print ("La Suma de los elementos Usando un ciclo for es:", ttl)

ttl = sum(T1)
print ("La Suma de los elementos Usando la funcion sum() es:", ttl)
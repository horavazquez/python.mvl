a = int(input("Ingrese un numero  A   "))
b = int(input("Ingrese otro numero B "))
c = int(input("Ingrese otro mas  C "))
 
 
def mayor_de_tres(a,b,c):
    if a > b and a > c:
        print("A es el mayor")
    elif b > a and b > c :
        print("B es el mayor")
    elif c > a and c > b:
        print("C es el mayor ")
 
 
def menor_que_tres(a,b,c):
    if a < b and a < c:
        print("A es el menor")
    elif b < a and b < c:
        print("B es el menor")
    elif c < a and c < b:
        print("C es el mejor")
 
 
if a == b or b == c or a == c:
        print("Numeros iguales ")
else:
    mayor_de_tres(a,b,c)
    menor_que_tres(a,b,c)

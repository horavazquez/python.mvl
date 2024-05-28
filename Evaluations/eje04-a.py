a = int(input("Ingrese un numero    "))
b = int(input("Ingrese otro numero  "))
c = int(input("Ingrese otro mas   "))

 
if a == b or b == c or a == c:
    print("Numeros iguales ")
 
elif a > b and a > c:
    print("A es el mayor")
elif b > a and b > c :
    print("B es el mayor")
elif c > a and c > b:
    print("C es el mayor ")
 
if a < b and a < c:
    print("A es el menor")
elif b < a and b < c:
    print("B es el menor")
elif c < a and c < b:
    print("C es el menor")
# 2. Algoritmo para encontrar el mayor de tres números. 
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

if a > b and a > c:
    mayor = a
elif b > c:
    mayor = b
else:
    mayor = c
print("El mayor de los tres números es:", mayor)
# 1. Algoritmo para sumar dos números. 
#  - Algortimo simple
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
suma = num1 + num2
print("La suma de", num1, "y", num2, "es:", suma)

# - Algoritmo con función
_num1 = int(input("Ingrese el primer número: "))
_num2 = int(input("Ingrese el segundo número: "))
def Suma(num1, num2):
    sum = num1 + num2
    return sum
print("La suma de", _num1, "y", _num2, "es:", Suma(_num1, _num2))
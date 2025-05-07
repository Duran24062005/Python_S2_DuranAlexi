# 10. Algoritmo para calcular el promedio de una lista de números. 
# - Algoritmo simple
ncn = int(input("Ingrese la cantidad de números: "))
suma = 0
for i in range(ncn):
    nums = float(input(f"Ingrese el número {i + 1}: "))
    suma += nums
promedio = suma / ncn   
print("El promedio es:", promedio)

#  - Algoritmo con lista
cn = int(input("Ingrese la cantidad de números: "))
numeros = []
for i in range(cn):
    num = float(input(f"Ingrese el número {i + 1}: "))
    numeros.append(num)
promedio = sum(numeros) / cn
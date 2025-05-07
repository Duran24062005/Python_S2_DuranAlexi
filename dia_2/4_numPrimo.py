# 4. Algoritmo para verificar si un número es primo. 
nIn = int(input("Ingrese un número: "))

if nIn <= 2:
    print("El número no es primo")

for i in range(2, nIn - 1):
    if nIn % i == 0:
        print(f"El número {nIn} no es primo")
        break
else:
    print(f"El número es primo")

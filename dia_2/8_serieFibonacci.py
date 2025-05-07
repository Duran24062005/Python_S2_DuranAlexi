# 8. Algoritmo para generar la serie de Fibonacci. 
nt = int(input("Ingrese el número de términos de la serie de Fibonacci: "))
a, b = 0, 1
print(f"a = {a}, b = {b}")
print("Serie de Fibonacci:")
for i in range(3, nt):
    nextTerm = a + b
    print(nextTerm, end=" ")
    a = b
    b = nextTerm
print()

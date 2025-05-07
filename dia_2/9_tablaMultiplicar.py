# 9. Algoritmo para generar una tabla de multiplicar. 
ng = int(input("Ingrese un número para generar su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {ng}:")
for i in range(1, 11):
    print(f"{ng} x {i} = {ng * i}")
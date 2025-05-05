# ######################
# #### Clase Día 1 #####
# ######################

# Imprimir en Pitón
print('Hola Mundo')

# Creación de variables
# 1. Dato tipo string
nombre = 'Alexi'
print(type(nombre))

# 2. Dato tipo número entero
numeroEntero = 1
# Variable tipada con dato entero
numeroEnteroConTipo:int = 19
print(type(numeroEntero))

# 3. Dato tipo numero real
numeroReal = 1.69
numeroRealConTipo:float = 1.69
print(type(numeroReal))

# 4. Dato de tipo Double
numeroPi = 1.9847596293854859
print(type(numeroPi))

# 5. Dato tipo booleano
booleano = True
booleanoConTipo:bool = True
print(type(booleano))

# 6. (SOLO PYTHON) Numeros complejos
numeroComplejo = complex('+1.23')
print(numeroComplejo)
print(type(numeroComplejo))

# Covertir numero int a float
numeroNuevo = float(numeroEntero)
print(numeroNuevo)
print(' ')

# ======================================================

#  Ciclos -- For, While --
# Ciclo for (Hasta)
for i in range(5):
    print(i)

# Ciclo for (Desde - Hasta)
for i in range(0, 5):
    print(i)

# Ciclo for (Desde - Hasta - Con Paso)
for i in range(0, 5, 1):
    print(i)

# Ciclo While
booleanNew = True
while (booleanNew == True):
    print('Sigo siendo verdadero ¡¡¡¡¡¡')
    booleanNew = False

booleanNew = True   
while (booleanNew):
    print('Sigo siendo verdadero ¡¡¡¡¡¡')
    booleanNew = False
# =========================================================

# Estructuras condicionales
# Condicional If - elseif - else
texto = 'user'
if texto == 'user':
    print('Sos user')

elif texto == 'admin':
    print('Sos admin')

else: 
    print('No sos admin')

    print('Sos admin')


# Desarrollado por : Alexi Durán Gómez - C.c: 1.067.031.983
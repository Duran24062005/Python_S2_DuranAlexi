# Python_S2_DuranAlexi

Este es un directorio para almacenar información sobre Python y lo aprendido en clases. Aquí encontrarás ejercicios, proyectos y recursos relacionados con el aprendizaje de este lenguaje.

## Índice de Carpetas y Subcarpetas

- **HackerRank**  
  Contiene ejercicios prácticos realizados en la plataforma HackerRank, organizados por dificultad y temática.
  - **Diccionarios**: Ejercicios de nivel básico.
  - **Listas**: Ejercicios de nivel intermedio.
  - **Ordenamiento_Algoritmos_Opcionales**: Ejercicios de nivel avanzado.
  - **Python-Ejercicios**: Ejercicios de nivel avanzado.

- **DuranAlexi_S2_Practic_Algoritms**  
  Carpeta destinada a proyectos desarrollados durante el curso, aplicando los conceptos aprendidos.
  - **Proyecto1**: Descripción breve del primer proyecto.
  - **Proyecto2**: Descripción breve del segundo proyecto.

- **Recursos**  
  Incluye materiales de apoyo como apuntes, enlaces útiles, y documentación relevante para el aprendizaje de Python.
  - **Documentación**: Archivos PDF y guías de referencia.
  - **Enlaces**: Lista de enlaces útiles para aprender Python.

- **Ejercicios**  
  Ejercicios adicionales realizados para reforzar los conceptos vistos en clase.
  - **Clase1**: Ejercicios relacionados con la primera clase.
  - **Clase2**: Ejercicios relacionados con la segunda clase.

¡Explora las carpetas y subcarpetas para más detalles sobre cada sección!

---

# Fundamentos de Python

## Índice

1. [Introducción a Python](#introducción-a-python)
2. [Variables y asignación](#variables-y-asignación)
3. [Tipos de datos básicos](#tipos-de-datos-básicos)
   - [Números](#números)
   - [Cadenas de texto (Strings)](#cadenas-de-texto-strings)
   - [Booleanos](#booleanos)
4. [Estructuras de datos](#estructuras-de-datos)
   - [Listas](#listas)
   - [Tuplas](#tuplas)
   - [Diccionarios](#diccionarios)
   - [Conjuntos](#conjuntos)
5. [Control de flujo](#control-de-flujo)
   - [Condicionales](#condicionales)
   - [Bucles](#bucles)
6. [Funciones](#funciones)
7. [Manejo de excepciones](#manejo-de-excepciones)
8. [Módulos y paquetes](#módulos-y-paquetes)

## Introducción a Python

Python es un lenguaje de programación interpretado, de alto nivel y de propósito general. Se caracteriza por su sintaxis clara y legible que enfatiza la facilidad de lectura del código.

```python
# Mi primer programa en Python
print("¡Hola, mundo!")
```

## Variables y asignación

En Python, las variables se crean cuando se les asigna un valor. No es necesario declarar su tipo previamente.

```python
# Asignación de variables
nombre = "Ana"
edad = 25
altura = 1.75
es_estudiante = True

# Python permite asignación múltiple
x, y, z = 1, 2, 3

# También es posible asignar el mismo valor a múltiples variables
a = b = c = 0

print(nombre)  # Imprime: Ana
print(edad)    # Imprime: 25
```

## Tipos de datos básicos

### Números

Python soporta varios tipos numéricos:

```python
entero = 42            # int (entero)
decimal = 3.14         # float (punto flotante)
complejo = 2 + 3j      # complex (número complejo)
binario = 0b1010       # representación binaria (valor: 10)
octal = 0o17           # representación octal (valor: 15)
hexadecimal = 0x1F     # representación hexadecimal (valor: 31)

# Operaciones básicas
suma = 5 + 3           # 8
resta = 10 - 4         # 6
multiplicacion = 6 * 7 # 42
division = 20 / 4      # 5.0 (siempre devuelve float)
division_entera = 20 // 6  # 3 (división entera)
modulo = 20 % 6        # 2 (resto de la división)
potencia = 2 ** 3      # 8 (2 elevado a 3)
```

### Cadenas de texto (Strings)

Las cadenas son secuencias inmutables de caracteres.

```python
# Definición de cadenas
cadena1 = 'Texto con comillas simples'
cadena2 = "Texto con comillas dobles"
cadena3 = '''Texto con 
            múltiples líneas'''

# Concatenación
nombre = "Juan"
saludo = "Hola, " + nombre + "!"  # Hola, Juan!

# Repetición
repeticion = "abc" * 3  # abcabcabc

# Acceso por índice (comienza en 0)
primera_letra = nombre[0]  # J

# Slicing (rebanado)
subcadena = nombre[1:3]    # ua

# Longitud
longitud = len(nombre)     # 4

# Métodos comunes de strings
mayusculas = nombre.upper()           # JUAN
minusculas = nombre.lower()           # juan
capitalizado = "python".capitalize()  # Python
reemplazo = "Hola mundo".replace("mundo", "Python")  # Hola Python
separacion = "uno,dos,tres".split(",")  # ['uno', 'dos', 'tres']
union = " - ".join(["A", "B", "C"])     # A - B - C
sin_espacios = "  texto  ".strip()      # texto
busqueda = "Python es genial".find("es")  # 7 (posición)
verificacion = "1234".isdigit()         # True
```

### Booleanos

Los valores booleanos representan verdadero o falso.

```python
verdadero = True
falso = False

# Operadores de comparación
igual = (10 == 10)            # True
distinto = (10 != 5)          # True
mayor = (10 > 5)              # True
menor = (10 < 20)             # True
mayor_igual = (10 >= 10)      # True
menor_igual = (5 <= 10)       # True

# Operadores lógicos
and_logico = True and False   # False
or_logico = True or False     # True
negacion = not True           # False

# Valores que se evalúan como False
print(bool(0))      # False
print(bool(""))     # False
print(bool([]))     # False
print(bool(None))   # False

# Valores que se evalúan como True
print(bool(1))      # True
print(bool("a"))    # True 
print(bool([0]))    # True
```

## Estructuras de datos

### Listas

Las listas son colecciones ordenadas y mutables de elementos.

```python
# Creación de listas
numeros = [1, 2, 3, 4, 5]
mixta = [1, "dos", 3.0, True]
anidada = [1, [2, 3], 4]
vacia = []
lista_rangos = list(range(1, 6))  # [1, 2, 3, 4, 5]

# Acceso por índice
primer_elemento = numeros[0]    # 1
ultimo_elemento = numeros[-1]   # 5

# Slicing
sublista = numeros[1:4]       # [2, 3, 4]
primeros_tres = numeros[:3]   # [1, 2, 3]
ultimos_tres = numeros[-3:]   # [3, 4, 5]
copia_lista = numeros[:]      # [1, 2, 3, 4, 5]

# Modificación
numeros[0] = 10              # [10, 2, 3, 4, 5]

# Métodos comunes para listas
numeros.append(6)             # [10, 2, 3, 4, 5, 6]
numeros.insert(1, 15)         # [10, 15, 2, 3, 4, 5, 6]
numeros.extend([7, 8])        # [10, 15, 2, 3, 4, 5, 6, 7, 8]
numeros.remove(15)            # [10, 2, 3, 4, 5, 6, 7, 8]
valor_eliminado = numeros.pop(0)  # valor_eliminado = 10, numeros = [2, 3, 4, 5, 6, 7, 8]
posicion = numeros.index(5)   # 3
conteo = numeros.count(3)     # 1
numeros.sort()                # [2, 3, 4, 5, 6, 7, 8]
numeros.reverse()             # [8, 7, 6, 5, 4, 3, 2]
numeros.clear()               # []

# Comprensión de listas (list comprehension)
cuadrados = [x**2 for x in range(1, 6)]  # [1, 4, 9, 16, 25]
pares = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
```

### Tuplas

Las tuplas son similares a las listas, pero son inmutables.

```python
# Creación de tuplas
coordenadas = (10, 20)
punto = (5,)  # Tupla de un solo elemento (requiere la coma)
tupla_mixta = (1, "dos", 3.0)
tupla_anidada = (1, (2, 3), 4)

# Acceso por índice (igual que las listas)
x = coordenadas[0]  # 10
y = coordenadas[1]  # 20

# Desempaquetado de tuplas
x, y = coordenadas  # x = 10, y = 20

# Métodos de tuplas
conteo = tupla_mixta.count("dos")  # 1
indice = tupla_mixta.index(3.0)    # 2

# Conversión entre listas y tuplas
lista_convertida = list(coordenadas)  # [10, 20]
tupla_convertida = tuple([1, 2, 3])   # (1, 2, 3)
```

### Diccionarios

Los diccionarios almacenan pares clave-valor.

```python
# Creación de diccionarios
persona = {
    "nombre": "Laura",
    "edad": 30,
    "profesion": "ingeniera"
}

telefonos = dict(casa="555-1234", trabajo="555-5678")
vacio = {}

# Acceso a valores
nombre = persona["nombre"]          # Laura
edad = persona.get("edad")          # 30
# Con get podemos especificar un valor por defecto si la clave no existe
hobby = persona.get("hobby", "No especificado")  # No especificado

# Modificación
persona["edad"] = 31
persona["hobby"] = "natación"

# Métodos comunes para diccionarios
claves = persona.keys()          # dict_keys(['nombre', 'edad', 'profesion', 'hobby'])
valores = persona.values()       # dict_values(['Laura', 31, 'ingeniera', 'natación'])
items = persona.items()          # dict_items([('nombre', 'Laura'), ('edad', 31), ('profesion', 'ingeniera'), ('hobby', 'natación')])

# Verificar existencia de clave
existe = "nombre" in persona     # True

# Eliminar elementos
del persona["hobby"]
profesion = persona.pop("profesion")  # Elimina y retorna el valor

# Diccionarios por comprensión
cuadrados_dict = {x: x**2 for x in range(1, 6)}  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### Conjuntos

Los conjuntos (sets) son colecciones no ordenadas de elementos únicos.

```python
# Creación de conjuntos
colores = {"rojo", "verde", "azul"}
numeros_set = set([1, 2, 3, 2, 1])  # {1, 2, 3}
conjunto_vacio = set()  # No se puede usar {}, ya que crea un diccionario vacío

# Operaciones de conjuntos
colores.add("amarillo")        # {"rojo", "verde", "azul", "amarillo"}
colores.remove("verde")        # {"rojo", "azul", "amarillo"}
colores.discard("negro")       # No da error si el elemento no existe

# Operaciones matemáticas de conjuntos
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

union = A | B                  # {1, 2, 3, 4, 5, 6}
interseccion = A & B           # {3, 4}
diferencia = A - B             # {1, 2}
diferencia_simetrica = A ^ B   # {1, 2, 5, 6}

# Verificar si un elemento está en el conjunto
existe = "rojo" in colores     # True
```

## Control de flujo

### Condicionales

Las estructuras condicionales permiten ejecutar código según se cumplan ciertas condiciones.

```python
# if-elif-else
edad = 18

if edad < 18:
    print("Menor de edad")
elif edad == 18:
    print("Justo en 18")
else:
    print("Mayor de edad")

# Operador ternario (expresión condicional en una línea)
mensaje = "Aprobado" if edad >= 18 else "No aprobado"

# Condicionales anidados
if edad >= 18:
    if edad < 21:
        print("Mayor de edad pero menor de 21")
    else:
        print("21 o mayor")
```

### Bucles

Los bucles permiten ejecutar código repetidamente.

```python
# Bucle for
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# Recorrer una lista
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

# Recorrer un diccionario
persona = {"nombre": "Juan", "edad": 30}
for clave in persona:
    print(clave, persona[clave])

# Alternativa usando items()
for clave, valor in persona.items():
    print(clave, valor)

# Bucle while
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# break y continue
for i in range(10):
    if i == 3:
        continue  # Salta a la siguiente iteración
    if i == 7:
        break     # Sale del bucle
    print(i)

# else en bucles (se ejecuta cuando el bucle termina naturalmente)
for i in range(5):
    print(i)
else:
    print("Bucle completado")

# enumerate (obtener índice y valor)
for indice, valor in enumerate(frutas):
    print(f"Índice {indice}: {valor}")
```

## Funciones

Las funciones permiten agrupar código reutilizable.

```python
# Definición de función básica
def saludar():
    print("¡Hola!")

# Función con parámetros
def saludar_persona(nombre):
    print(f"¡Hola, {nombre}!")

# Función con parámetros por defecto
def saludar_personalizado(nombre, mensaje="¡Hola!"):
    print(f"{mensaje}, {nombre}")

# Función que retorna un valor
def sumar(a, b):
    return a + b

# Función con múltiples valores de retorno
def operaciones(a, b):
    suma = a + b
    resta = a - b
    return suma, resta  # Devuelve una tupla

# Llamada a funciones
saludar()
saludar_persona("María")
saludar_personalizado("Carlos", "Buenos días")
resultado = sumar(5, 3)  # 8
s, r = operaciones(10, 4)  # s = 14, r = 6

# Argumentos arbitrarios
def suma_varios(*args):
    return sum(args)

print(suma_varios(1, 2, 3, 4))  # 10

# Argumentos de palabras clave arbitrarios
def describir_persona(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

describir_persona(nombre="Ana", edad=25, ciudad="Madrid")

# Combinación de tipos de parámetros
def funcion_completa(param1, param2, *args, **kwargs):
    print(f"Parámetros regulares: {param1}, {param2}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

# Funciones lambda (anónimas)
cuadrado = lambda x: x ** 2
print(cuadrado(5))  # 25

# Uso común de lambda con funciones como map y filter
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))  # [1, 4, 9, 16, 25]
pares = list(filter(lambda x: x % 2 == 0, numeros))  # [2, 4]
```

## Manejo de excepciones

El manejo de excepciones permite manejar errores de forma controlada.

```python
# Bloque try-except básico
try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
    print(f"El resultado es {resultado}")
except ValueError:
    print("Error: Debes ingresar un número válido")
except ZeroDivisionError:
    print("Error: No puedes dividir por cero")

# Capturar múltiples excepciones en una línea
try:
    # Código que puede generar error
    pass
except (ValueError, TypeError) as e:
    print(f"Ocurrió un error: {e}")

# Bloque else (se ejecuta si no hay excepciones)
try:
    numero = int("123")
except ValueError:
    print("No es un número válido")
else:
    print("Conversión exitosa")

# Bloque finally (se ejecuta siempre)
try:
    archivo = open("datos.txt", "r")
except FileNotFoundError:
    print("El archivo no existe")
finally:
    print("Este bloque siempre se ejecuta")
    # Si abrimos el archivo, debemos cerrarlo aquí

# Crear excepciones personalizadas
class MiErrorPersonalizado(Exception):
    def __init__(self, mensaje="Error personalizado"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

# Lanzar una excepción
def verificar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    if edad > 120:
        raise MiErrorPersonalizado("Edad no válida")
```

## Módulos y paquetes

Los módulos y paquetes permiten organizar el código y reutilizarlo.

```python
# Importar un módulo completo
import math
resultado = math.sqrt(16)  # 4.0

# Importar funciones específicas
from math import sqrt, pi
resultado = sqrt(16)  # 4.0
print(pi)  # 3.141592653589793

# Importar con alias
import math as m
resultado = m.sqrt(16)  # 4.0

# Importar todo (no recomendado generalmente)
from math import *
resultado = sqrt(16)  # 4.0

# Crear un módulo propio (archivo: mi_modulo.py)
"""
def saludar(nombre):
    return f"Hola, {nombre}"

PI = 3.14159
"""

# Importar módulo propio
import mi_modulo
saludo = mi_modulo.saludar("Ana")

# Módulos comunes de la biblioteca estándar
import os           # Funciones del sistema operativo
import sys          # Funciones y parámetros específicos del sistema
import datetime     # Tipos de fecha y hora
import json         # Codificación y decodificación JSON
import random       # Generación de números aleatorios
import re           # Expresiones regulares
```

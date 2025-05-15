# Aquí van las funciones que se utilizaran para pedir las entradas al usuario y la preparacion de diccionario,
# para enviarlas a el archivo funciones.py y que allá se guarde de una vez.
from funciones import *

'''
    Funcion del controlador para Crear usuario  
'''
def crear_user():
    print("#######################")
    print("#### Crear Persona ####")
    print("#######################")

    nombre = input('DIga el nombre: ')
    apellido = input('DIga el apellido: ')
    edad = input('DIga el edad: ')
    catPhone = int(input('Diga la cantidad de telefonos: '))

    diccionarioUsuario = {
        "id": 0,
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "telefonos": [] 
    }
        

    for j in range(catPhone):
        code = int(input('Código: '))
        phone = int(input('Número: '))
        work = input('Tipo: ')

        # Variable para crear el diccionario de la información de telefotno
        data = {
            "codigo": code,
            "numero": phone,
            "tipo": work
        }
        diccionarioUsuario["telefonos"].append(data)
    
    create_user(diccionarioUsuario)

'''
    Función Leer - Read : Función del controlador para mostrar un solo usuario por su ID.
'''
def leer_user():
    print("###################################")
    print("#### Mostrar Persona por si Id ####")
    print("###################################\n")
    id = int(input('Por favor, escriba el id del usuario que busca: '))
    print(read_user(id))
        


'''
    Función Leer - Read : Función del controlador para mostrar a todos los usuarios.
'''
def listar_user():
    print("#####################################")
    print("#### Mostrar a todas las Persona ####")
    print("#####################################\n")
    print(databaseList)
    print('\n')

# TODO
'''
    Función Actualizar - Update : Función del controlador.
'''
def actualizar_user():
    print("\n#####################################")
    print("#### Actualizar Persona por su Id #####")
    print("#######################################\n")
    id = int(input('Por favor, escriba el id del usuario que desea actualizar: '))
    user = read_user(id)
    
    if not user:
        print("Usuario no encontrado.")
        return

    print("¿Qué campo desea modificar?")
    print("1. Nombre")
    print("2. Apellido")
    print("3. Edad")
    print("4. Teléfonos")
    print("5. Todos los campos")

    opcion = input("Seleccione una opción: ")
    nuevos_datos = {}

    if opcion == "1":
        nuevos_datos["nombre"] = input("Nuevo nombre: ")
    elif opcion == "2":
        nuevos_datos["apellido"] = input("Nuevo apellido: ")
    elif opcion == "3":
        nuevos_datos["edad"] = input("Nueva edad: ")
    elif opcion == "4":
        nuevos_telefonos = []
        catPhone = int(input("Cantidad de teléfonos: "))
        for j in range(catPhone):
            code = int(input("Código: "))
            phone = int(input("Número: "))
            tipo = input("Tipo: ")
            nuevos_telefonos.append({
                "codigo": code,
                "numero": phone,
                "tipo": tipo
            })
        nuevos_datos["telefonos"] = nuevos_telefonos

    elif opcion == "5":
        nuevos_datos["nombre"] = input("Nuevo nombre: ")
        nuevos_datos["apellido"] = input("Nuevo apellido: ")
        nuevos_datos["edad"] = input("Nueva edad: ")
        nuevos_telefonos = []
        catPhone = int(input("Cantidad de teléfonos: "))
        for j in range(catPhone):
            code = int(input("Código: "))
            phone = int(input("Número: "))
            tipo = input("Tipo: ")
            nuevos_telefonos.append({
                "codigo": code,
                "numero": phone,
                "tipo": tipo
            })
        nuevos_datos["telefonos"] = nuevos_telefonos

    else:
        print("Opción no válida.")
        return

    actualizado = update_user(id, nuevos_datos)
    if actualizado:
        print("Usuario actualizado exitosamente.\n")
    else:
        print("Error al actualizar el usuario.\n")


'''
    Función Eliminar - Delet : Función del controlador.
'''
def eliminar_user():
    print("\n###################################")
    print("######## Eliminar Persona por su ID #########")
    print("#####################################\n")
    id = int(input('Por favor, escriba el id del usuario que busca: '))
    return delete_user(id)

# Desarrollado por Alexi Durán Gómez : C.C-1.067.031.983

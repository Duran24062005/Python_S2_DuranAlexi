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
    return read_user(id)
        


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
    id = int(input('Por favor, escriba el id del usuario que busca: '))
    user = read_user(id)
    if user:
        print('1. para modificar el usuario')
        print(f'\t nombre: {user["nombre"]}')
        print(f'\t apellido: {user["apellido"]}')
        print(f'\t edad: {user["edad"]} \n')
        print('1. para modificar el telefono del usuario')

        modified = input('Elija una opción a modificar')

        if (modified == 1):
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

        elif(modified == 2):
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
    return update_user(id, data)

'''
    Función Eliminar - Delet : Función del controlador.
'''
def eliminar_user():
    id = int(input('Por favor, escriba el id del usuario que busca: '))
    return delete_user(id)

# Desarrollado por Alexi Durán Gómez : C.C-1.067.031.983
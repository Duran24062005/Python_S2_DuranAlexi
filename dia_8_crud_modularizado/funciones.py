# Funciones de CRUD
# CLAE
from database import databaseList

# Función Crear - Create
def create_user(user:dict):
    if user:
        databaseList.append(user)
        return True
    else:
        print('Error al enviar el usuario.')
        return False

# Función Leer - Read
def read_user(id:int):
    for i in range(len(databaseList)):
        if id == databaseList[i]['id']:
            return databaseList[i]
        else:
            print('User no encontrado. \n')
# TODO
# Función Actualizar - Update
def update_user(id, data: dict):
    user = read_user(id)
    if user:
        print('1. para modificar el usuario')
        print(f'\t nombre: {user["nombre"]}')
        print(f'\t apellido: {user["apellido"]}')
        print(f'\t edad: {user["edad"]} \n')
        print('1. para modificar el telefono del usuario')

        modified = input('Elija una opción a modificar')

# TODO
# Función Eliminar - Delet
def delete_user():
    pass


# Desarrollado por Alexi Durán Gómez : C.C-1.067.031.983
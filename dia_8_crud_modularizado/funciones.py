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
    for i, user in enumerate(databaseList):
        if user['id'] == id:
            return user
        else:
            print('User no encontrado. \n')
# TODO
# Función Actualizar - Update
def update_user(id, data: dict):
    for i, user in enumerate(databaseList):
        if user["id"] == id:
            # Actualizar solo los campos que se encuentran en 'data'
            for key in data:
                user[key] = data[key]
            databaseList[i] = user  # Aplicar la actualización
            return True
    print("Usuario no encontrado para actualizar.")
    return False


# TODO
# Función Eliminar - Delet
def delete_user(id: int):
    for i, user in range(len(databaseList)):
        if user['id'] == id:
            deleted = databaseList[i].remove(id)


# Desarrollado por Alexi Durán Gómez : C.C-1.067.031.983
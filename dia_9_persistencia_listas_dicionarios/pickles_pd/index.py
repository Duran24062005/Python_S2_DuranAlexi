import pickle

data = {
    "nombres": ["Ana", "Luis"],
    "edades": [20, 25]
}

# ruta de archivo
sub_carpeta = "/home/administrador/Escritorio/Campuslands/Python_S2_DuranAlexi/dia_9_persistencia_listas_dicionarios/pickles_pd/datos.pkl"

# Subir los datos
with open(sub_carpeta, "wb") as archivo:
    pickle.dump(data, archivo)

# Ver los datos cargados
with open(sub_carpeta, "rb") as archivo:
    datos_cargados = pickle.load(archivo)

print(datos_cargados)

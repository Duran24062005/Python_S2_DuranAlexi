# Persistencia de datos

# Iniciamos creando un diccionario
my_dict = {
    "nombres": ['Ana', 'Eliza'],
    "edades": [20, 31]
}


# Y ahora lo vamos a guardar en el archivo dat.json
# Para eso importamos el modulo json
import json

# Declaramos la ruta del archivo
from pathlib import Path
ruta_Actual = Path.cwd()
print(ruta_Actual)
sub_carpeta = "/home/administrador/Escritorio/Campuslands/Python_S2_DuranAlexi/dia_9_persistencia_listas_dicionarios/json/datos.json"

# LO abrimos el archivo en modo de escritura mediante el archivo
# Cabe aclara que si no existe el archivo se creara solo.
with open(sub_carpeta, "w") as archivo:
    # Procedemos a guardar los datos
    json.dump(my_dict, archivo)
    print('Datos guardados exitosamente')

# Desarrollado por Alexi Durán Gómez : C.C-1.067.031.983
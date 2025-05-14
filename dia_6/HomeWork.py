# ##########################
# #### Clase Dia 6 ######
# ##########################
# Diccionarios
#Un DICccionario  es una colección de elementos , donde cada elementos insertado tiene una llave úntica, 
# la cual va acompañada de un valor 

##Diccionario con listas
diccionarioRobusto={
    "id":1,
    "nombre":"Pedro",
    "apellido":"Gómez",
    "edad":25,
    "telefonos":[
        {
            "codigo":57,
            "numero":3023019865,
            "tipo":"trabajo"
        },
        {
            "codigo":1,
            "numero":3983054625,
            "tipo":"personal"
        }
    ]
}
diccionarioRobusto2={
    "id":2,
    "nombre":"Corpus",
    "apellido":"Bejarano",
    "edad":27,
    "telefonos":[{"codigo":58,"numero":2323057565,"tipo":"trabajo"}
                 ,{"codigo":22,"numero":6857493658,"tipo":"personal"}]
}
listaRobusta=[]
listaRobusta.append(diccionarioRobusto)
listaRobusta.append(diccionarioRobusto2)


# print("")# 
# print("")
# print(listaRobusta)
# print("")
# print("")
#print(listaRobusta[0]["telefonos"][1]['numero'])

# for i in range(len(listaRobusta[0]["telefonos"])):
    # if(listaRobusta[0]["telefonos"][i]['tipo']=="trabajo"):
        # print(listaRobusta[0]["telefonos"][i]['numero'])
# print("")
# print("")
# numeroPrimeraPersona=listaRobusta[0]["telefonos"][1]['numero']
# tipoNumeroPP=listaRobusta[0]["telefonos"][1]['tipo']
# print(str(numeroPrimeraPersona)+ tipoNumeroPP)


booleanito = True
while(booleanito):
    print("#################")
    print("#### Librería de personas ####")
    print("#################")
    #CRUD (CREATE , READ , UPDATE & DELETE)
    print("1. Crear Persona")
    print("2. Mostrar todas las personas")
    print("3. Mostrar a una persona individual")
    print("4. Actualizar a una persona en específico")
    print("5. Eliminar a una persona en específico")
    print("6. Cerrar programa")
    opcionUsuario=int(input("Escoja una opción (Numérica):"))

    if(opcionUsuario==1):
        print("#################")
        print("#### Crear Persona ####")
        print("#################")
        diccionarioVacio={}
        nombre = input('DIga el nombre: ')
        apellido = input('DIga el apellido: ')
        edad = input('DIga el edad: ')
        catPhone = int(input('Diga la cantidad de telefonos: '))

        diccionarioUsuario = {
            "id": 0,
            "nombre":nombre,
            "apellido":apellido,
            "edad":edad,
            "telefonos":[] 
        }
        

        for j in range(catPhone):
            code = int(input('Código: '))
            phone = int(input('Número: '))
            work = input('Tipo: ')

            # Variable para crear el diccionario de la información de telefotno
            data = {
                "codigo":code,
                "numero":phone,
                "tipo":work
            }
            diccionarioUsuario['telefonos'].append(data) # Aquí
        
        counter = 0
        id_user = 0
        # Ciclo para encontrar recorrer la lista de usuariso ya creados
        for i in range(len(listaRobusta)):
            counter += 1
            # Condicional para ver si coincide el id actal del iterador con uno ya existente
            # Y se asigna el que si
            if listaRobusta[i] == diccionarioUsuario['nombre']:
                id_user = counter  # N sé como asignar el numero del indice, porque así asigna es el contenido

        diccionarioUsuario['id'] = id_user
        listaRobusta.append(diccionarioUsuario)
        print(f'Persona {nombre} creada correctamente.')

    elif(opcionUsuario==2):
        for i in range(len(listaRobusta)):
            print("#################")
            print("#### Persona #",i+1," ####")
            print("#################")
            print("ID:", listaRobusta[i]["id"])
            print("Nombre:",listaRobusta[i]["nombre"])
            print("Apellido:",listaRobusta[i]["apellido"])
            print("Edad",listaRobusta[i]["edad"])
            
            for q in range(len(listaRobusta[i]["telefonos"])):
                print("---------------------------")
                print("Telefono#",q+1,":")
                print("#### - Código:",listaRobusta[i]["telefonos"][q]["codigo"])
                print("#### - Numero:",listaRobusta[i]["telefonos"][q]["numero"])
                if(listaRobusta[i]["telefonos"][q]["tipo"] == "personal"):
                    print("#### - Tipo: Es su número Personal")
                else:
                    print("#### - Tipo: Es su número de Trabajo")
                
                print("---------------------------")
    elif(opcionUsuario==3):
        print("#################")
        print("#### Mostrar persona individual ####")
        print("#################")
        idPersona=int(input("Ingrese el ID de la persona que desea ver:"))
        for i in range(len(listaRobusta)):
            if(listaRobusta[i]["id"]==idPersona):
                print("ID:", listaRobusta[i]["id"])
                print("Nombre:",listaRobusta[i]["nombre"])
                print("Apellido:",listaRobusta[i]["apellido"])
                print("Edad",listaRobusta[i]["edad"])
                
                for q in range(len(listaRobusta[i]["telefonos"])):
                    print("---------------------------")
                    print("Telefono#",q+1,":")
                    print("#### - Código:",listaRobusta[i]["telefonos"][q]["codigo"])
                    print("#### - Numero:",listaRobusta[i]["telefonos"][q]["numero"])
                    if(listaRobusta[i]["telefonos"][q]["tipo"] == "personal"):
                        print("#### - Tipo: Es su número Personal")
                    else:
                        print("#### - Tipo: Es su número de Trabajo")
                    
                    print("---------------------------")

    elif(opcionUsuario==4):
        print("#################")
        print("#### Actualizar a una persona en específico ####")
        print("#################")

        idPersona = int(input('Por favor, escriba el ID del usuario: '))

        # for i range(len(listaRobusta)):
            # if(listaRobusta)
            
    elif(opcionUsuario==6):
        print("Chaousssss")
        booleanito=False
    else:
        print("No es una opción válida")

# Ejercios numeros primos
n = int(input('Escribe un numero: '))


    
    
#Desarrollado por Alexi Durán Gómez : C.C-1.067.031.983
# Siguentes puntos
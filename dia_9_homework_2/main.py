if __name__ == '__main__':

    program = True
    while program:
        print("##################################")
        print("###### Librería de personas ######")
        print("##################################")
        print(' ')
        #CRUD (CREATE , READ , UPDATE & DELETE)
        print("1. Crear Persona")
        print("2. Mostrar todas las personas")
        print("3. Mostrar a una persona individual")
        print("4. Actualizar a una persona en específico")
        print("5. Eliminar a una persona en específico")
        print("6. Cerrar programa")
        opcionUsuario=int(input("Escoja una opción (Numérica): "))
        print(' ')

        if (opcionUsuario == 1):
            # crear_user()
            pass

        elif (opcionUsuario == 2):
            # listar_user()
            pass

        elif (opcionUsuario == 3):
            # leer_user()
            pass

        elif (opcionUsuario == 4):
            # actualizar_user()
            pass

        elif (opcionUsuario == 5):
            # eliminar_user()
            pass

        elif (opcionUsuario == 6):
            print("\n#######################################")
            print("## Gracias por utilizar el software ###")
            print("##### Librería de personas ############")
            print("#######################################\n")
            print(' ')
            program = False

        else: 
            print('\n  ¡¡Opción no valida!!')
            print('¡Elija una opción valida! \n')


# Desarrollado por Alexi Durán Gómez : C.C-1.067.031.983
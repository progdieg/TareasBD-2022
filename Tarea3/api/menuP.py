import os 

def Menu():

    print("Menu Principal:  \n 1. Mostrar Persona \n 2. Insertar Persona \n 3. Modificar Perona \n 4. Eliminar Persona \n 5. Salir")
    
    menuP=0
    while menuP != 5:

        menuP=int(input("Digite opcion =>  "))
        os.system('cls')

        if menuP == 1:
            print("------------ Mostrar Persona ---------- \n")
            
            print("|  Nombre  |  Apellido  |   Direccion  |  Telefono  |   Sueldo   |  Transporte | Alimentacion  |  Pension  |  Salud  | ")



        elif menuP == 2:
            print("------------ Insertar Persona ---------- \n")

            print("|  Nombre  |  Apellido  |   Direccion  |  Telefono  |   Sueldo   |  Transporte | Alimentacion  |  Pension  |  Salud  | ")

        elif menuP == 3:
            print("------------ Modificar Persona ---------- \n")

            print("|  Nombre  |  Apellido  |   Direccion  |  Telefono  |   Sueldo   |  Transporte | Alimentacion  |  Pension  |  Salud  | ")
    
        elif menuP == 4:
            print("------------ Eliminar Persona ---------- \n")

            print("|  Nombre  |  Apellido  |   Direccion  |  Telefono  |   Sueldo   |  Transporte | Alimentacion  |  Pension  |  Salud  | ")

        elif menuP == 5:
            print("5. Salir \n")
        else:
         print("Digite una opcion valida")   
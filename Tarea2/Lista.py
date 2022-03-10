def listaColegio():
    nombre=["Juan", "Camilo", "Diego", "Sebastian"]
    edad=[15,17,19,16]
    doc=[1067845679, 3389276457, 1212099087, 98875647839]
    id=[31223,77654,12090,98902]
    año=["Octavo Grado", "Decimo grado", "Onceavo grado", "Noveno grado"]
    
    print("Lista de nombres: ",nombre)
    print("Lista de edades: ",edad)
    print("Lista de documento de identidad: ",doc)
    print("Lista de Identificacion Estudiantil: ",id)
    print("Lista de Grado Actual",año)

    print("")
    print("Datos Estudiantiles")
    print("")

    print("Perfil de Juan")
    print("Nombre: ",nombre[0], "|" , "Edad: ",edad[0],"|" , "Doc identidad: ",doc[0],"|" , "Id Estudiantil: ",id[0],"|" ,"Año: ", año[0],"|")
    print("")

    print("Perfil de Camilo")
    print("Nombre: ",nombre[1], "|" , "Edad: ",edad[1],"|" , "Doc identidad: ",doc[1],"|" , "Id Estudiantil: ",id[1],"|" ,"Año: ", año[1],"|")
    print("")

    print("Perfil de Diego")
    print("Nombre: ",nombre[2], "|" , "Edad: ",edad[2],"|" , "Doc identidad: ",doc[2],"|" , "Id Estudiantil: ",id[2],"|" ,"Año: ", año[2],"|")
    print("")

    print("Perfil de Sebastian")
    print("Nombre: ",nombre[3], "|" , "Edad: ",edad[3],"|" , "Doc identidad: ",doc[3],"|" , "Id Estudiantil: ",id[3],"|" ,"Año: ", año[3],"|")
    print("")

def main():
    listaColegio()

if __name__ == '__main__':
    main()
# Menu persona 
from api.menuP import *
 
def listadoPersonas():
    class Persona():
        def __init__(self): 
            self.nombre=input("Ingrese el nombre:   ")
            self.apellido=input("Ingrese el apellido:  ")
            self.direccion=input("Ingrese la direccion: ")
            self.telefono=input("Ingrese el telefono:  ")
        def mostrarListadoPer(self):
            print(f"Nombre: {self.nombre}    Apellido: {self.apellido}")




def main():
    Menu()
   


if __name__ == "__main__":
    main()
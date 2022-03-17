def main():
    class Persona():
        def __init__(self): 
            self.nombre=input("Ingrese el nombre:   ")
            self.apellido=input("Ingrese el apellido:  ")
            self.direccion=input("Ingrese la direccion: ")
            self.telefono=input("Ingrese el telefono:  ")
        
        def mostrarPersona(self):
            print(f"Nombre: {self.nombre} {self.apellido}")

    #Herencia
    class Empleado(Persona):
        def __init__(self):
            super().__init__()
            self.__sueldo=float(input("Ingrese el sueldo: "))
            self.pension=4
            self.salud=3.375
            self.alimen=0
            self.transp=0
            if self.__sueldo < 2000000:
                self.alimen=80000
                self.transp=60000
            else:
                self.alimen=0
                self.transp=0
            
            self.pension=self.__sueldo*0.04
            self.salud=self.__sueldo*0.0375 
            
            
        def mostrarEmpleado(self):
            super().mostrarPersona
            print(f"Sueldo: {self.__sueldo}")
            print(f"Transporte: {self.transp}")
            print(f"Alimentacion:   {self.alimen}")
            print(f"Pension:  {self.pension}")
            print(f"Salud:  {self.salud}")

        def mostrarDevengado(self):
            devengado= self.alimen + self.transp
            self.__sueldo+=devengado
            print(f"Devengado:  {self.sueldodev}")
        
        def mostrarDeduccion(self):
            deduccion=self.pension+self.salud
            self.__sueldo-=deduccion
            print(f"Deduccion:  {self.sueldodeduc}")
            


    empleado1=Empleado()
    empleado1.mostrarEmpleado()
    empleado1.mostrarDevengado()
    empleado1.mostrarDeduccion()


if __name__=="__main__":
    main()


    #alimentacion +trasn se suma al sueldo = Devengado

    #pension + salud se resta al sueldo

    #<2000000 se paga alimen 80000 
    #transpor 60000
    #>2000000 alimen 0 y transp 0 
    #pension 4%
    #salud 3.375%
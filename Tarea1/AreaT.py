#sin ingreso por teclado

def calcularAreaTriangulo():
    print("Datos asignados")
    base=2
    altura=2
    area=base*altura/2
    print(f"La base del triangulo es: {base}, la altura es: {altura} siendo su base de: {area}")

#Ingreso por teclado

def calcularAreaTrianguloTec():
    print("Datos ingresados por teclado")
    baseTec=int(input("Digite la base del triangulo: "))
    alturaTec=int(input("Digite la altura del triangulo: "))
    areaTec=baseTec*alturaTec/2
    print(f"La base del triangulo es: {baseTec}, su altura es de: {alturaTec} siendo su base de: {areaTec}")

def main():
    calcularAreaTriangulo()
    calcularAreaTrianguloTec()

if __name__ == "__main__":
    main()
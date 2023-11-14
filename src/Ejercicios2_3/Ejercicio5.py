def pedirContraseña():
    contraseña=input("Introduce una contraseña: ")
    return contraseña

def validarContraseña(contraseña):
    salir=False
    while not salir:
        entrada=input("Vuelve a introducir la contraseña: ")
        try:
            if(contraseña!=entrada):
                raise NameError
            print("Las dos contraseñas son iguales")
            salir=True
        except:
            print("Error, no coincide con la contraseña")

def main():
    contraseña=pedirContraseña()
    validarContraseña(contraseña)

if(__name__=="__main__"):
    main()

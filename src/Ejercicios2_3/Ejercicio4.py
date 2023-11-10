def pedirNumero():
    salir=False
    while not salir:
        entrada=input("Introduce un número: ")
        try:
            n=int(entrada)
            if n<0:
                raise ValueError
            print("número válido")
            salir = True
        except ValueError:
                print("Error, numero no válido")

def main():
    pedirNumero()

if(__name__=="__main__"):
    main()
def pedirEdad():
    salir=False
    while not salir:
        entrada=input("Introduce tu edad: ")
        try:
            n=int(entrada)
            if n < 0:
                raise ValueError
            salir = True
        except ValueError:
            print("Error, edad no válida")
    
    return n

def contarEdades(edad):
    cont=1
    while(cont<=edad):
        if(cont!=edad):
            print(cont, end=",")
        else:
            print(cont)
        cont+=1

def main():
    edad=pedirEdad()

    contarEdades(edad)

if(__name__=="__main__"):
    main()
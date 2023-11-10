def pedirNumero():
    salir=False
    while not salir:
        entrada=input("Introduce un número: ")
        try:
            n=int(entrada)
            if n < 0:
                raise ValueError
            salir = True
        except ValueError:
            print("Error, numero no válido")
    
    return n

def cuentaAtras(n):
    while(n>=0):
        if(n!=0):
            print(n,end=",")
        else:
            print(n)
        n-=1

def main():
    n=pedirNumero()

    cuentaAtras(n)

if(__name__=="__main__"):
    main=()
    
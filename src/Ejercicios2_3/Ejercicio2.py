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

def contarImpares(n):
    cont=1
    while(cont<=n):
        if((cont==n-1 or cont==n) and cont%2!=0):
            print(cont,end="")
        elif(cont%2!=0):
            print(cont,end=",")
        cont+=1
    

def main():
    n=pedirNumero()

    contarImpares(n)

if(__name__=="__main__"):
    main()
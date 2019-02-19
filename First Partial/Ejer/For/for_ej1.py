#print("\n")
#Escribir del 1 al 10
#for x in range(1,11,1):
#    print(x)

def imprimir_nombre(nombre):
    for x in range(5):
        print(nombre)


def numeros_suma(cantidad):
    sum=0
    for x in range(cantidad):
        sum+=float(input("Please give me a number"))
    print(sum)

def numeros_suma(cantidad):
    par=0
    ina=0
    for x in range(cantidad):
        numero=float(input("Dame un numero, sea par o impar, quedan %5.0f numeros" %(x)))
        if numero%2==0:
            par=1+par
        else:
            ina+=1
    print(par, " fueron pares")
    print(ina,"fueron inpares")

def suma_naturales(cantidad):
    numero=0
    cantidad+=1
    for x in range(cantidad):
        numero+=x

    print(numero)

#nombre=str(input("Escribe un nombre:\n"))
#imprimir_nombre(nombre)

#cantidad=int(input("How many times?"))
#numeros_suma(cantidad)

#cantidad=int(input("How many numbers?"))
#numeros_suma(cantidad)


cantidad=int(input("Cuantos numeros naturales se sumaran?"))
suma_naturales(cantidad)

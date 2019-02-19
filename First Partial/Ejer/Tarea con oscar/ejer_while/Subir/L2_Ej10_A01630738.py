#Julio Rosales Oliden
#A01630738

#se pide el numero
numero=float(input("Inserte un numero para checar si es un numero perfecto \n"))
#asignamos variables para evitar problemas con el programa
n=0
suma=0
numero_dividido=numero
#cuando el numero no sea 0 el programa correra
if numero!=0:
    #checara que el divisor no sea mas grande que la mitad del dividendo para dividirlo
    while n<=numero/2:
            n+=1
            if numero_dividido%n==0:
                suma+=n
#en caso de que el numeor ya no sea divisible o no sea 1 se dira que es perfecto
    if suma/numero==1 and numero!=1:
#se dira si el numero es perfecto o no
        print("El numero es perfecto")
    else:
        print("el numero no es perfecto")
else:
    print("el numero no es perfecto")

#aprendi lo que era un numero perfecto y como calcularlo con un python

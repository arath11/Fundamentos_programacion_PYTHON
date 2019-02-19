#Julio Arath Rosales Oliden
#A01630738

#se pide el numero 
numero=int(input("inserte un numero natural: \n"))
#cuando el numero no sea 1, se dividira el numero para ver si da un residiuo si lo da es un numero impar y lo multiplicara por tres y le sumara 1
#en caso de ser par lo dividira entre 2 hasta que llegue a 1
while numero!=1:
    if numero%2==0:
        numero=numero/2
        print("%20.0f" %(numero))
    elif numero%2==1:
        numero=numero*3+1
        print("%20.0f" %(numero))

#use por primera vez el !=l, otra opcion seria un not(numero==1), pero la que use es mas corta

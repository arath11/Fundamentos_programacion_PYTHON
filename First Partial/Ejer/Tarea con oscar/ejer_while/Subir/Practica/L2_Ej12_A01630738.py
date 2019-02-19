#Julio Rosales Oliden
#A01630738

numero=float(input("Inserta el numero \n"))
digitos=1
numero=abs(numero)
while 9<=numero or numero<=-9:
    numero=numero/10
    digitos+=1


print("el numero tiene "+ str(digitos) + " digitos")

#Aprendi a usar el abs (absoluto)

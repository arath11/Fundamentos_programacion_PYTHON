#Julio Rosales Oliden A01630738

#se dice lo que hace el programa
print("Escribe un numero, se sumara hasta que escribas un numero negativo")
num=0
dato_user=0
#si  el dato ingresado por el usuario es mayor o igual que cero el programa correra la suma
while dato_user>=0:
    dato_user=int(input("Escribe un numero \n"))
    #compara si el dato es mayor que 0 para hacer la suma
    if dato_user>=0:
        num+=dato_user

print("El numero sumado resulto en "+ str(num))

#aprendi a usar un if adentro ded un while

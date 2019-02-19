def suma(cantidad):
    contador=0
    suma_=0
    for x in range(cantidad):
        contador=contador+1
        if x%2==0:
            suma_=-contador+suma_
        else:
            suma_=contador+suma_
        print(suma_)






#cantidad=int(input("Cuantos numeros naturales se sumaran?"))
#suma(cantidad)




def __n__(numero):
    for x in range(1,11,1):
        multiplicacion=numero*x
        #print(numero, "x", x, "=", multiplicacion)
        print(f"{numero:2d} x {x:2d} = {multiplicacion:3d}")

#numero=int(input("Cual tabla quieres que se realize?"))
#__n__(numero)


gustos=["durazno", "pozole", "pan", "René"]
for cosa in gustos:
    print("a mi me gustta el: %s" %(cosa))

cadena="muy facil programar en python"
for i in range(len(cadena)):
    print("letra {0:2d}: {1}" .format(i, cadena[i]))

palabra=str(input("dame la primera  palabra"))
palabr=str(input("dame la segunda  palabra"))

suma_vocales_1=0
suma_vocales_2=0
for i in range(len(palabra)):
    if palabra[i]=="a" or palabra[i]=="e" or palabra[i]=="i" or palabra[i]=="o" or palabra[i]=="u":
        suma_vocales_1+=1
        #print(f"la vocal es {palabra[i]} ")
for i in range(len(palabr)):
    if palabr[i]=="a" or palabr[i]=="e" or palabr[i]=="i" or palabr[i]=="o" or palabr[i]=="u" :
        suma_vocales_2=suma_vocales_2+1
        #print(f"la vocal es {palabra[i]} ")
if suma_vocales_1<suma_vocales_2:
    print(f"la segunda palabra {palabr} con {suma_vocales_2} vocales, tiene mas vocales que {palabra} con {suma_vocales_1} vocales")
elif suma_vocales_1>suma_vocales_2:
    print(f"la primera palabra {palabra} con {suma_vocales_1} vocales, tiene mas vocales que {palabr} con {suma_vocales_2} vocales")
else:
    print("son iguales")

lista=[1,2,3,4,5]
for i in range(len(lista)):
    lista[i]=lista[i]*lista[i]
print(lista)

lista1=[1,2,3,5,6,7,8]
lista2=[2,7]
lista3=[]
for a in range(len(lista1)):

    for b in range(len(lista2)):
        if lista1[a] == lista2[b]:
            #lista3.append(str(lista1(a)))
            print("el numero", str(lista1[a]), "es igual a el numero ", str(lista2[b]))
        else:
            print("el numero", str(lista1[a]), "no es igual a el numero ", str(lista2[b]))
#print(lista3)


palabra=str(input("Dame la palabra"))
for i in range(len(palabra[::2])):
    print(i)
    print(palabra[i])
    print()


lista5=["hola", "no",  "h1"]
total_h=0
for indice in lista5:
    if lista5[indice][0]=="h" or lista5[indice][0]=="H":
        lista5[indice]=str("Julio")
        total_h+=1
#print(f"Totla de h es {total_h}")
print(lista5)

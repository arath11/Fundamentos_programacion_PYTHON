archivo=open("archivo1.txt", "r", encoding="UTF-8")
for i in archivo:
    print(i.rstrip())
archivo.close()

for i in range(len(lista)):
    suma = 0
    for j in range(1, 4):
        if j == 1:
            suma = lista[i][j] * .25
        elif j == 2:
            suma += lista[i][j] * .4
        else:
            suma += lista[i][j] * .30
    lista[i].append(suma)

# Julio Arath Rosales Oliden
# A01630738

def lee_archivo():
    """lEE EL ARCHIVO """
    try:
        archivo=open("calif.csv", "r+", encoding="UTF-8")
    except:
        print("No se encuentra el archivo ")
    else:
        calif=[]
        for linea in archivo:
            lista=[]
            linea_split=linea.split(",")
            evitar_nombre=0
            for elemento in linea_split:
                if evitar_nombre!=0:
                    lista.append(int(elemento))
                else:
                    lista.append(str(elemento))
                evitar_nombre+=1
            calif.append(lista)
        archivo.close()
        return calif


def promedio_parcial(lista,n):
    """Esta funcion regresa el promemdio parcial del grupo"""
    calif=0
    for i in range(len(lista)):
        calif+=lista[i][n]
    calif=calif/len(lista)
    return calif


def despliega_finales(lista):
    """Esta funcion imprime a pantalla la calificacion de cada alumno"""
    for i in range(len(lista)):
        suma=0
        for j in range(1,5):
            if j == 1:
                suma= lista[i][j]*.25
            elif j == 2:
                suma += lista[i][j]*.4
            else:
                suma += lista[i][j] * .30
        lista[i].append(suma)
        print(f"{lista[i][0]} tiene promedio de: {lista[i][4]}")


def calif_final(lista):
    try:
        archivo = open("calif.csv", "w+", encoding="UTF-8")
    except:
        print("No se encontro el archivo")
    else:
        if len(lista[0])==4:
            """Anterior funcion de calcula finales """
            lista=a(lista)
            """for i in range(len(lista)):
                suma = 0
                for j in range(1, 4):
                    if j == 1:
                        suma = lista[i][j] * .25
                    elif j == 2:
                        suma += lista[i][j] * .4
                    else:
                        suma += lista[i][j] * .30
                lista[i].append(suma)"""
        for i in lista:
            string = ""
            contador = 0
            for j in i:
                contador += 1
                if contador < 5:
                    string += str(j) + ","
                else:
                    string += str(j)
            string +="\n"
            print(string)
            archivo.write(string)
        archivo.close()

def a(lista):
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
    return lista


lista=lee_archivo()
calif_final(lista)
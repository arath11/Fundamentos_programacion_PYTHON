# Julio Arath Rosales Oliden
# A01630738

lista = [["Oscar1", 80, 90, 100], ["Oscar2", 80, 90, 100], ["Oscar3", 80, 90, 100]]

def calif_final(lista):
    """Esta funcion usa las calificaciones para calcular el promedio final de cada alumno"""
    for i in range(len(lista)):
        suma=0
        for j in range(1,4):
            if j == 1:
                suma= lista[i][j]*.25
            elif j == 2:
                suma += lista[i][j]*.4
            else:
                suma += lista[i][j] * .30
        lista[i].append(suma)
    return lista


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
        for j in range(1,4):
            if j == 1:
                suma= lista[i][j]*.25
            elif j == 2:
                suma += lista[i][j]*.4
            else:
                suma += lista[i][j] * .30
        lista[i].append(suma)
        print(f"{lista[i][0]} tiene promedio de: {lista[i][4]}")


def suma_matrices(lista1,lista2):
    """Esta funcion suma dos tuplas"""
    lista3=[]
    for i in range(len(lista1)):
        tupla=[]
        for j in range(len(lista1[i])):
            tupla.append(lista1[i][j]+lista2[i][j])
        lista3.append(tupla)
    return lista3


def escalar(lista,n):
    """Esta funcion recibe ua tupla y la multiplican por el numero dado"""
    for i in range(len(lista)):
        lista[i]=lista[i]*n
    return lista


def traspuesta(lista):
    """Esta funcion recibe una matriz y regresa su traspuesta"""
    nueva_lista=[]
    for i in range(len(lista[0])):
        filas=[]
        for j in range(len(lista)):
            filas.append(lista[j][i])
        nueva_lista.append(filas)
    print(nueva_lista)


def triangular_inferior(lista):
    """Esta funcion usa tupla para verificar si es es triangular inferior"""
    for ren in range(len(lista)):
        for columna in range(len(lista[ren])):
            if columna > ren:
                if lista[ren][columna]!=0:
                    return False
    return True


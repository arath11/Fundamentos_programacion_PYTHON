# Julio Arath Rosales Oliden
# A01630738
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





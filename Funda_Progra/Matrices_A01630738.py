#A01630738
#Julio Arath Rosales Oliden

#Funciones
def creaMatriz1(n):
    """Esta funcion recibe un numero n para darle el valor de -1 a la matriz n*n"""
    matriz=[]
    for reng in range(n):
        lista = []
        for num in range(n):
            lista.append(-1)
        matriz.append(lista)
    return matriz


def creaMatriz2(n):
    """ Esta funcion crea un matriz n*n para darle el valor de la localidad de la columna"""
    matriz=[]
    for i in range(n):
        lista=[]
        numero = 0
        for a in range(n):
            lista.append(numero)
            numero += 1
        matriz.append(lista)
    return matriz


def creaMatriz3(n):
    """Esta funcion recibe un numero y hace una matriz para hacer las listas con el mismo valor de la fila"""
    matriz=[]
    numero=1
    for i in range(n):
        lista=[]
        for a in range(n):
            lista.append(numero)
        matriz.append(lista)
        numero += 1
    return matriz


def creaMatriz4(n):
    """La función crea una matriz"""
    matriz=[]
    for fila in range(n):
        lista=[]
        primer_contador=1
        contador = 0
        for columna in range(n):
            lista.append(1+fila+(contador*n))
            contador+=1
            primer_contador+=1
        matriz.append(lista)
    return matriz


def cuentaPares(lista):
    """Esta funcion recibe una lista y checa la cantidad de pares en la lista y lo regresa"""
    num_pares=0
    for i in range(len(lista)):
        for a in range(len(lista[i])):
            if lista[i][a]%2==0:
                num_pares+=1
    return num_pares


def sumaMatriz(lista):
    """Esta funcion suma la matriz que recibe por si misa """
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            lista[i][j]=lista[i][j]+lista[i][j]
    return lista


def cuentaPositivos(lista):
    """Esta regressa una lista de  numeros que son mayores a 0 """
    lista_positivos=[]
    for i in range(len(lista)):
        for a in range(len(lista[i])):
            if lista[i][a]>0:
                lista_positivos.append(lista[i][a])
    return lista_positivos


def cambiaNegativos(lista):
    """Cambia los negativos por ceros """
    for i in range(len(lista)):
        for a in range(len(lista[i])):
            if 0>lista[i][a]:
                lista[i][a]=0
    return lista


def cuentaRepeticiones(lista, numero):
    """Esta funcion regresa la cantidad de numeros que se repiten en la lista"""
    repeticiones=0
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i][j]==numero:
                repeticiones+=1
    return repeticiones


def busca(lista, numero):
    """ Esta funcion regresa true si el numero se encuentra en la lista"""
    for i in lista:
        if numero in i:
            return True
    return False


def sumaMayores5(lista):
    """Etsa funcion regresa la sumatoria de los numeros mayores a 5"""
    suma=0
    for i in range(len(lista)):
        for a in range(len(lista[i])):
            if lista[i][a]>5:
                suma+=lista[i][a]
    return suma


def cambiaCeros(lista):
    """Cambia los ceros por la posicion en la que se encuentran """
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j]==0:
                lista[i][j]=i+j
    return lista




lista = [[1,1,1],
         [2,2,2],
         [3,3,3]]

listaA=[[1,2,3],[4,5],[6,7],[0,0]]
print(cambiaCeros(listaA))
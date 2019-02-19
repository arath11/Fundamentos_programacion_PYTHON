#Julio Arath Rosales Oliden
#a01630738
#importamos librerias
from random import randint

#comienzan las definiciones
def locura(palabra):
    """Esta funcion cambia las letras de un string; e por 3, las a por 4 y las o por h, las demas letras las deja como estaban, regresando un string """
    nueva=""
    for letra in palabra:
        if letra in "e":
            nueva+="3"
        elif letra in "a":
            nueva+="4"
        elif letra in "o":
            nueva+="h"
        else:
            nueva+=letra
    return nueva


def espaciado(palabra):
    """Genera un espacio entre cada letra, regresando un string """
    nueva=""
    for letra in palabra:
        nueva+=letra
        nueva+=" "
    return nueva


def tirada(numero):
    """Recibe un numero para depues dar dos tiradas de dado y sumarseloas, regresa la variable numeri """
    for i in (0,1):
       numero+=randint(1,6)
    return numero


def separa_guiones(palabra, numero):
    """Recibe una palabra, creara un string para agregar cierca cantidad de guiones dependiendo el numero que se incerte
    regresa la nueva palabra en formad e string"""
    suma=1
    nueva=""
    tamaño=0
    sumatoria=0
    cantidad=0
    guiones=0
    for letra in palabra:
        cantidad=cantidad+1
    for letra in palabra:
        if numero/suma==1:
            guiones=guiones+1
            suma=1
            nueva += letra
            if cantidad > guiones+1:
                nueva+="-"
        else:
            guiones+=1
            sumatoria += 1
            nueva+=letra
            suma+=1
    return nueva


def con_N_letras(lista,n):
    """la funcion busca comparan cuantas palabras de una lista tienen mas o igual de la cantidad de letras introducida
    regrresara un numero con la cantidad de las palabras que lo sobrepase """
    lista2=""
    letra=0
    cantidad=0
    for i in lista:
       for b in i:
           letra+=1
       if n <= int(letra):
           cantidad+=1
       letra=0
    return cantidad


def invierte(lista):
    """Esta funcion recibe una lista, crea otra lista en la cual se ponen los datos invertidos de la primer lista, regresa
    la segunda lista"""
    lista2=[]
    n = len(lista)
    for i in range(len(lista)-1, -1, -1,):
        lista2.append(lista[i])
    return lista2


def los_3_menores(lista):
    """Recibe una listam ordena los datos y regrresa una lista con los tres datos menores """
    lista.sort()
    lista2=[]
    for i in range(0,3):
        lista2.append(lista[i])
    return lista2


def duplicada(lista):
    """Recibe una lista, despues crea otra lista en la que agregan todos los datos de la primer lista pero multiplicados por dos"""
    lista2=[]
    for i in range(len(lista)):
        lista2.append(lista[i]*2)
    return lista2


""" ejercicios hechos en clase 1,6,12 y las pruebas de mis programas 
def mayores_N(lista, n):
    contador=0
    for elemnto in lista:
        if elemnto>n:
            contador+=1
    return contador


def vocales_Mayusculas(cadena):
    lista=[]
    for letra in cadena:
        if letra in "aeiou":
            lista.append(letra.upper())
            print(letra,1)
        else:
            lista.append(letra)
            print(letra,2)
    nueva="".join(lista)
    return nueva


def solo_3(lista):
    for posicion in range(len(lista)):
        lista[posicion]=lista[posicion][0:3]
    return lista

lista=[4,3,5,7,10,1,3,5,7]
print(invierte(lista))

lista=[4,3,5,7,10,1,3,5,7]
print(duplicada(lista))
print(los_3_menores(lista))

n=6
print(con_N_letras(lista,n))
palabra="paracaidas"
numero=2
print(separa_guiones(palabra,numero))

numeros=[3,6,8,9,10,6,7]
num=8
cuantos=mayores_N(numeros,num)
print(f"numeros mayores a {num} son: {cuantos}")

palabra="ana leticia"
vocales=vocales_Mayusculas(palabra)
print(vocales)
lista2=["hola", "luis", "la casa", "cabriel"]
print(solo_3(lista2))

lista=["oscar", "gabo", "julio", "oscar"]
cosa="g"
print(empiezan_Con(cosa))

palabra="aereo"
print(locura(palabra))
print(espaciado(palabra))
"""

lista=[[a,b],
       [c,d]]

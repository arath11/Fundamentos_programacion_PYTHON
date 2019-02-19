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

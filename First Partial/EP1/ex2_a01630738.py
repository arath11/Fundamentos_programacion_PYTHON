#A01630738
#Julio Rosales
lista1=[1,2,3,4,5,6,7,8,9,10]
sumatoria=0
cantidad=0
#tomara cada valor de la lista para poder hacelo esa cantidad de ocaciones
for i in lista1:
        #compara si el numero en la posicion i -1 es mayor a 5 para despues sumarlo sumatoria
        if lista1[i-1]>5:
            cantidad+=1
            sumatoria+=lista1[i-1]
#imprime la sumatoria
print(f"La sumatoria de los numeros mayores a 5 es {sumatoria:10d}")
print(f"La canitdad de numeros mayores fueron {cantidad:10d}")
#Imprime el numero mayor de la lista
max_lista=max(lista1)
print(f"El numero mayor de toda la lista es {max_lista:10d}")
#Aprendi a comparar adentro de un for con una lista

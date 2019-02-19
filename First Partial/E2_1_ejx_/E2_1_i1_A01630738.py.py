#Julio Arath Rosales Oliden
#A01630738
#en esta parte pedimos la palabra por el usuario y ahora creamos un string vacio
cadena=input("Escribe la palabra para cambiar las e por 3 y las a por 4 y las o por h : \n")
cambiada=""
#por cada letra en la cadena se comparara si contiene A o a o E o e o O o o para cambiarlo por 3 o 4
#depues se agrega el 3 o 4 o se deja la misma letra que ya tenia la palabra
for letra in cadena:
    #si la letra tiene a o A se agregara un 4 al string
    if letra in "AaáÁ":
        cambiada=cambiada+str(4)
    #en caso de tener e o E en la letra se agrega  al string un 3 en lugar de la letra
    elif letra in "eEéÉ":
        cambiada=cambiada+str(3)
    #Cuando la letra tenga o o O se agregara una h en lugar de la letra
    elif letra in "oOÓó":
        cambiada=cambiada+"h"
    #Si no se cumple ninguna de las condiciones anteriores se agregara la misma letra al string
    else:
        cambiada=cambiada+letra
#Este metodo funciona pero no es el metodo mas optimo porque siempre se creando un nuevo string
#Seria más aeficiente si se realizara con listas
print(f"La nueva palabra es {cambiada}")

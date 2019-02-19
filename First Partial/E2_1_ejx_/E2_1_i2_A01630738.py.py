#Julio Arath Rosales Oliden
#A01630738

#Se pide que al usuario una palabra, despues se crea un string vacio para poder modificarlo despues
cadena=input("Escribe la palabra, cambiaremos las vocales minusculas por MAYUSCULAS: \n")
cambiada=""
#Por la cantidad de letras en la palabra se comprara si tienen una vocal en minusculas para despues cambiarla a mayusculas en el nuevo string
#En caso de no tener una vocal se colocara en el nuevo string  se colocara la misma letra
for letra in cadena:
    #Si la letra contiene la vocal se le agregara una A al string creado
    if letra in "a":
        cambiada=cambiada+"A"
    #Cuando la letra e este en la palabra se le agregara al string una E
    elif letra in "e":
        cambiada=cambiada+"E"
    #En caso de tener una i en la letra se le agregara una I al string cambiada
    elif letra in "i":
        cambiada=cambiada+"I"
    #Ahora se compara si tiene una o en la letra, despues se agrega una O en el nuevo string
    elif letra in "o":
        cambiada=cambiada+"O"
    #Si aparece la una u en la letra, se agregara  una U en el string
    elif letra in "u":
        cambiada=cambiada+"U"
    #En caso de no cumplir con alguna de la anteriores condiciones solo se agrefara la misma laetra al string creado
    else:
        cambiada=cambiada+letra
print(f"La nueva palabra es {cambiada}")

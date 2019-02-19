#Julio Arath Rosales Oliden
#A01630738

#Validación del numeor
def entero_validacion(incognito):
    while True:
        numero=input(f"Inserta la medida de la {incognito} en centimetros:")
        try:
            numero=int(numero)
            return numero
        except ValueError:
            print("La entrada no es un numero, por favor ingresalo de nuevo")

#Presentacion del programa
print(f"Este programa calcula el area de un triangulo")

#Pregunta sobre la base del triangulo
incognito="base"
base = entero_validacion(incognito)

#Pregunta sobre la altura del triangulo
incognito="altura"
altura = entero_validacion(incognito)

#Calculo
area=base*altura/2

#Imprime a pantalla el resultado
print(f"El area del triangulo es de {area:.2f} cm")
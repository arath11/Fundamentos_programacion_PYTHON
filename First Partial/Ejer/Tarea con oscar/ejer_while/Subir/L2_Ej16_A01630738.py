#Julio Rosales Oliden A01630738
import random

#Pedimos el numero aleatorio
numero_adivinar=random.randint(0, 100)
print("Jugaras adivinar un numero entre 0 y 100, suerte (tienes 7 intentos)")
i=7
#Corremos el while para que despues de 7 intentos se detenga
while i>=1:
    i=i-1
    dato_user=float(input("Escribe un numero \n"))
    #comparamos el dato dado por el usuario y el numero random, dira se es mas
    #grande o chico o si gano incluso en el primer intento
    if dato_user>numero_adivinar:
        print("El numero aleatorio es más pequeño")
        print("Te quedan ", i, " intentos")
    elif dato_user<numero_adivinar:
        print("El numero aleatorio es más grande")
        print("Te quedan ", i, " intentos")
    elif dato_user==numero_adivinar:
        print("FELICIDADES GANASTE")
        i=-10
#aprendi a usar random

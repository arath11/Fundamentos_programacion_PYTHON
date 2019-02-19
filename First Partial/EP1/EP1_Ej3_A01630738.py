
#Pedimos las calificacion para empezar
print("Este programa calcula cuantos alumnos pasaron \n cuantos reprobaron y el promedio grupal \n cuando la calificacion del alumno sea menor de 70  no paso\nCuando inserte una calificacion negativa o 0 el programa dejara de correr ")
calificacion=float(input("Inserte la calificacion del alumno:"))
alumnos_aprobados=0
alumnos_reprobados=0
cantidad_alumnos=0
promedio_suma=0
#comparamos si la calificacion es 0 negativa, en caso de serla el programa correra, despues vemos en que rango de calificacion se encuentra el alumno para saber si aprobo o no y sacar el promedio general
while calificacion!=0 and calificacion>-1:
    if calificacion>=70:
        alumnos_aprobados+=1
    elif calificacion<70:
        alumnos_reprobados+=1
    cantidad_alumnos+=1
    promedio_suma=calificacion+promedio_suma
    calificacion=float(input("Inserte la calificacion del alumno:"))

promedio=promedio_suma/cantidad_alumnos
print("\n-------------------------------------------\nLa cantidad de alumnos aprobados fue:" +str(alumnos_aprobados) +"\nLa cantidad de alumno reprobados fue:" +str(alumnos_reprobados)+"\nEl promedio general del grupo fue de:" +str(promedio)+"\n-------------------------------------------")

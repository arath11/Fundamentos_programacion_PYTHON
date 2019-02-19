#Julio Arath Rosales Oliden
#A01630738

#En la primera parte se pide la cantidad de alumnos en el grupo
#Despues asignamos una varieble que cuente la calificacion grupal a 0 para hacer la sumatoria de esta
estudiantes=int(input("Este programa calcula el promedio por estudiante y por grupo\nEscribe el numero de estudiantes en el grupo:"))
calif_gsuma=0

#Ahora se realizara el programa dependiendo de la cantidad de alumnos sean del grupo
for i in range(estudiantes):
    #ahora se pregunta la calificacion del alumno para depues hacer el promedio y se agrega
    #a un promedio grupal que es dividido entre la cantidad de alumnos para dar el promedio grupal
    print("---------------------------------------")
    calif_1=float(input("Escribe la primera calificacion:"))
    calif_2=float(input("Escribe la segunda calificacion:"))
    calif_3=float(input("Escribe la tercera calificacion:"))
    calif=(calif_1+calif_2+calif_3)/3
    calif_gsuma+=calif
    print(f"El promedio del alumno {i+1:2d} fue {calif}")
calif_grupal=calif_gsuma/estudiantes
print("---------------------------------------")
print(f"La calificación grupal fue de {calif_grupal:3.2f}")


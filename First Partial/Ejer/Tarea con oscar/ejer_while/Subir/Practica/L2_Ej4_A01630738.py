#Julio Rosales Oliden A01630738
#se pide el dato
numero=float(input("Ingrese un numeor si que este entre 1 y 10, si no lo esta lo repetira: \n"))

#se repetira en caso de no ser un numeor en el rango uno y diez
while not(numero>=1 and numero<=10):
  numero=float(input("Ingrese un numeor si que este entre 1 y 10, si no lo esta lo repetira: \n"))

#le agradece a la persona que no gastara más tiempo ingresando un numeor que no fuera entre uno y diez
print("gracias por escribir un numero entre 1 y 10")

 #aprendi a usar el not() con el uso while

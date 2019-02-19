#Oscar Miranda A01630791
#Julio Arath Rosales Oliden A01630738

#Se piden las variables
print("Escribiras 3 numeros en el orden que desees, ")
variable_1=float(input("Inserta el primeros de los tres numeros \n"))
variable_2=float(input("Inserta el segundo de los tres numeros \n"))
variable_3=float(input("Inserta el tercero de los tres numeros \n"))

#Se compara las variables para ver que la primera variable sea mas pequeña que la segunda variable y esta que la tercera, en caso de que no sea asi
#Se dice que los numeros no fueron introduciods de manera descendiente
if variable_1<variable_2 and variable_2<variable_3:
    print("Los numeros fueron introducidos de manera descendiente", variable_1, " < ", variable_2, " < ", variable_3)
else:
    print("Los numeros no fueron introducidos de manera descendiente")
#Aprendi junto a Oscar a usar if con and en lugar de if anidaddos :)

#Julio Arath Rosales Oliden
#A01630738

#Se piden los datos
temp_fahr=float(input("Inserta los grados en fahrenheit, seran convertidos en Celsius y Kelvin \n"))
#Se convierte a Celsius y Kelvin
temp_cel=(5/9)*(temp_fahr-32)
temp_kel=(5/9)*(temp_fahr-32)+273
#Se imprimen los datos
print("La temperatura em gredos celsius es {0:2.3f} " .format(temp_cel))
print("La temperatura en grados kelvin es {0:2.3f}" .format(temp_kel))



#Esta actividad me ayudo a mejorar el uso de distintos metodos de impresion
#https://www.thoughtco.com/temperature-conversion-formulas-609324

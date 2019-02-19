#Julio Arath Rosales Oliden
#A01630738

import math
#Se piden los datos
lado_l=float(input("Inserta la medida del lado L \n"))
lado_h=float(input("Inserta la altura del prisma \n"))
#Se saca el area, sumando las areas de los triangulos y los rectangulos
area_base=(math.sqrt(3)/4)*(lado_l**2)
area_lado=(lado_h*lado_l)
area_todo=(area_base*2)+(area_lado*3)
#Se imprime el area
print("El area de todo el prisma triangular regular es " + str(area_todo) + " cm.")

#Aprendi a imprimir de diferente manera, lo que creo que es mas util a solo comas 
#http://www.universoformulas.com/matematicas/geometria/area-prisma-triangular/

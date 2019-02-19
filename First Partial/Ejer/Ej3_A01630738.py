#Julio Arath Rosales Oliden
#A01630738
import math

#Se piden los datos al usuario
altura=int(input("Inserta la altura a la que quiere llegar  \n"))
angulo=int(input("Inserta la medida del angulo de la escalera \n"))
angulo_radianes=math.radians(angulo)
largo_escalera=altura/math.sin(angulo_radianes)
print("El largo necesasrio de la escalera para llegar es de \n %15.5f°" %(largo_escalera))

#aprendi a usar programas para hacer problemas relacionados con senos, cosenos y tangentes. Tambien lo usare para que haga por mi mis trabajos de fisica

#Julio Arath Rosales Oliden
#A01630738

def esconde(string):
    """Esta funciona regresaa un nuevo string en el que se cambian las b por las 8
    las i por 1 y las """
    nuevo=""
    for letra in string:
        if letra in "b":
           nuevo+="8"
        elif letra in "i":
            nuevo+="1"
        elif letra in "e":
            nuevo+="9"
        else:
            nuevo+=letra
    return nuevo


def area_prisma(l,h):
    """Esta funcion regresa el area de un prisma,  """
    area_rectangulos=l*h*3
    area_triangulo=((3**.5)*(l**2))/2
    area_total=area_rectangulos+area_triangulo
    return area_total

"""string="biep"
print(esconde(string))
l=1
h=1
print(area_prisma(l,h))"""
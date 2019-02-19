#Julio Arath Rosales Oliden
#A01630738
#se piden y asignan las cantidades de x,y y z y tambien que se quiere realizar con estos vcectores
print("Hola, calcularemos la suma, diferencia, producto escalar o producto vectorial \n de dos vectores en tres dimensiones ")
opcion=str(input("para escoger por favor seleciona una opcion \n Suma (1) \n Diferencia (2) \n prosucto escalar (3) \n producto vectorial (4) \n"))

#se realizara las sumas, diferencias, productos escalar y productos vectoriales de los vectores
while opcion=="1" or opcion=="2" or opcion=="3" or opcion=="4":
    print("\n ahora escribiras el primer vector" )
    x1=float(input("Escribe el vector x1:"))
    y1=float(input("Escribe el vector y1:"))
    z1=float(input("Escribe el vector z1:"))
    print("\n  ahora escribiras el segundo vector" )
    x2=float(input("Escribe el vector x2:"))
    y2=float(input("Escribe el vector y2:"))
    z2=float(input("Escribe el vector z2:"))

    if opcion=="1":
        suma_x=(x1+x2)
        suma_y=(y1+y2)
        suma_z=(z1+z2)
        print("la suma de los vector es ", suma_x, " en x + ", suma_y, "en y + ", suma_z, "en z.")
    elif opcion=="2":
        resta_x=(x1-x2)
        resta_y=(y1-y2)
        resta_z=(z1-z2)
        print("la resta de los vector es ", resta_x, " en x + ", resta_y, "en y + ", resta_z, "en z.")
    elif opcion=="3":
        multi_x=(x1*x2)
        multi_y=(y1*y2)
        multi_z=(z1*z2)
        print("El producto escalar de los vector es ", multi_x, " en x + ", multi_y, "en y + ", multi_z, "en z.")
    elif opcion=="4":
        producto_1=(y1*z2)-(z1*y2)
        producto_2=(z1*x2)-(x1*z2)
        producto_3=(x1*y2)-(y1*x2)
        print("El producto vectorial es ", producto_1, " en x + ", producto_2, "en y + ", producto_3, "en z.")
    else:
        break
    opcion=str(input("para escoger por favor seleciona una opcion \n Suma (1) \n Diferencia (2) \n prosucto escalar (3) \n producto vectorial (4) \nPara salir escriba ortra cosa"))

#aprendi a usar el break, realmente es útil para que no se repita el proceso

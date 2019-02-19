# A01630738 Julio Arath Rosales Oliden

# Esta funcion convierte de segundos a minutos a horas a dias


def __segundos__(seg):
    # divide la cantidad de seg entre 60 pero de enteros y despues saca el residuo de los segundos entre 60 y repite
    # igual con las Horas
    # despues repetira el mismo proceso pero ahora de horas a dias dividiendolo entre 24 enteros y sacando el residuo
    # entre 24 de horas
    minutos = seg // 60
    seg = seg % 60
    horas = minutos // 60
    minutos = minutos % 60
    dias = horas // 24
    horas = horas % 24
    print(f"Dias:    {dias:3.0f} \nHoras:   {horas:3.0f} \nMinutos: {minutos:3.0f} \nSegundos:{seg:3.0f} ")


def __pies__(x, y):
    if y == "y":
        p = x * .333333
        return p
    elif y == "p":
        p = x * 12
        return p
    elif y == "m":
        p = x * .3048
        return p
    else:
        print("Use otra letra")


def __volumen_esfera__(x):
    return 4 / 3 * 3.14 * ((x) ** 3)


def __multiplo__(x, y):
    if x % y == 0:
        return True
    else:
        return False


def __area__(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** (1 / 2)
    return area


def __comparacion__():
    if numero_1 < numero_2:
        return -1
    elif numero_1 == numero_2:
        return 0
    elif numero_1 > numero_2:
        return 1


def __menu__():
    print("\nTenemos 5 programas, el primero convierte de segundos a minutos, horas y dias (1) \nEl segundo programa convierte de pies a yardas, metros o pulgadas (2)")
    print("El tercero saca el volumen de una esfera solo con el radio (3)\nEl cuarto cheaca que un numero sea multiplo del primero (4) \nEl quinto compara entre dos numeros cual es el mayor (5)\n6 para salir" )
    aopc = input("Dame tu  opcion:\n")
    return aopc

respuesta=0

while respuesta!=6:
    respuesta=__menu__()
    if respuesta == "1":
        respuesta_1 = float(input("Escribe la cantidad de segundos que convertiremos a horas, dias, minutos y segundos:\n"))
        __segundos__(respuesta_1)

    elif respuesta == "2":
        conver = str(input("Dime a que lo convertire a yardas (y), pulgadas (p) o metros (m):\n"))
        if conver in "ypm":
            cuanto = float(input("Cuanto convertire?\n"))
            dato = __pies__(1, conver)
            print(f"La cantidad de pies a {conver} es {dato} ")
        else:
            print("Opcion incorrecta de medida")

    elif respuesta == "3":
        radio = float(input("Dame el area del circulo para sacar el volumen :\n"))
        volumen = __volumen_esfera__(radio)
        print(f"El volumen del circulo es  {volumen}")

    elif respuesta == "4":
        numero_mul = float(input("Inserta el numero para checar si es multiplo del siguiente numero \n Primer numero:"))
        multiplo = float(input("Inserta el posible multiplo:"))
        if __multiplo__(25, 5):
            print(f"En efecto, el numero {multiplo} es un multiplo de {numero_mul}")
        else:
            print(f"Lamentablemente el numero {multiplo} no es un multiplo del numero {numero_mul}")
    elif respuesta == "5":
        print(
            "Escribiras dos numeros, si el primero es menor al segundo se escribira -1\n0 son iguales\n1 si el primer argumento es mayor al segundo")
        numero_1 = float(input("Dame el primer numero:\n"))
        numero_2 = float(input("Dame el segundo numero:\n"))
        datos=__comparacion__()
        if (datos) == 1:
            print(f"El primer numero {numero_1} es mayor al segundo {numero_2}")
        elif datos == 0:
            print(f"Ambos numeros son iguales")
        elif datos == -1:
            print(f"El primer numero {numero_1} es menor que el segundo {numero_2}")

    elif respuesta== "6":
        print("Gracias por usar este programa :)")
        break
    else:
        print("Opcion invalida sol acepto datos del 1 al 6")


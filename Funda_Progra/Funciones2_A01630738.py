#Julio Arath Rosales Oliden
#A01630738

#Se importa la libreria tiempo
import time
#import progressbar
#creamos algunas variables necesarias para el programa y una lista vacia para los multiplos en comun
multiplo=0
sumatoria=0
lista1=[]



def energia(masa):
    '''Esta funcion recibe la masa de un objeto y la multiplica por la veolicad de la luz al cuadtrado para dar E y
    regresarla'''
    e=masa*3.0e9**2
    return e

def barra_progreso(segundos):
    '''Esta funcion hace un a barra para contar el tiempo pasado'''
    contador=0
    equis=""
    while contador<(segundos/10):
        contador+=1
        time.sleep(10)
        equis+="x"
        print(f"{equis}")
    print("El tiempo ha concluido")


def ofertas(x,y,limite):
    '''este programa calcula las ofertas de una tarjeta para llamar al extanjero '''
    multiplo_x=[]
    multiplo_y=[]
    multiplos_comun=[]
    for i_x in range(1,limite//x+1):
        multiplo_x.append(x*1)
    for i_y in range(1, limite // y + 1):
        multiplo_y.append(y * 1)
    for element_x in range(len(multiplo_x)):
        for element_y in range(len(multiplo_y)):
            if multiplo_x[element_x]==multiplo_y[element_y]:
                multiplos_comun.append(multiplo_x[element_x])



def multiplos_comunes(n1, n2, limite):
    '''Esta funcion calcula los multiplos comunes de dos numero hasta un limite definido por el usuario'''
    multiplo=0
    sumatoria=0
    while multiplo<limite:
        sumatoria+=1
        multiplo=n1*n2*sumatoria
        if  multiplo<limite:
            lista1.append(multiplo)
    return lista1


def __menu__():
    '''Esta funcion corre el programa de menu para tomar una ocpion de las funciones anteriorers'''
    print("Hola seleciona una opcion\n(1) Es una ecuacion de E=mc**\n(2) la segunda es un programa que saca el comun multiplo")
    print("(3) es un programa que consigue las ofertas\n(4)El cuarto programa es una barra de progrerso que mide 100 segundos \n(5)Te saca del progerama")
    aopc = input("Dame tu  opcion:\n")
    return aopc


#Programa principal
#Para correr las funciones anteriores primero asignamos una variable para poder compararla en un while y salir del loop
respuesta=0
#Ahora corrermos la funcion de menu para conseguir la selecion del usuario y depsues corrermos un if
#para comarar la variable respuesta con el posible resultado y asi correr el programa deseado
while respuesta!="5":
    respuesta = __menu__()
    if respuesta == "1":
        masa=int(input("Cual es la masa del objeto en kilogramos?\n"))
        emc=energia(masa)
        print(f"E={emc}")
    elif respuesta=="2":
        print("Inserta los siguientes valores:")
        n1=float(input("El primer numero:\n"))
        n2 = float(input("El segundo numero:\n"))
        limite = float(input("Limite:\n"))
        multiplo_print=multiplos_comunes(n1,n2,limite)
        print(multiplo_print)
    elif respuesta=="3":
        cantidad=float(input("Inserta la cantidad de saldo que abonaste 3, 25, 50 o 100 para conocer que oferta especial obtendras\n"))
        print(ofertas(cantidad))
    elif respuesta == "4":
        print("Selecionaste barra de progreso")
        segundos=float(input("¿Cuantos segundos seran?:\n"))
        barra_progreso(segundos)
    elif respuesta == "5":
        print("")
    else:
        print("Porfa, seleciona algo valido")
    print("")
    print("")
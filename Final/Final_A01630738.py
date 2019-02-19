#Julio Arath Rosales Oliden
#A01630738

def menor_ingresado():
    print("Ingrese un numero, mientras no sea cero lo ingresara denuevo")
    numero = float(input("Ingrese un numero :\n"))
    menor_numero=numero
    while numero!=0:
        numero=float(input("Ingrese otro numero :)\n"))
        if numero<menor_numero and numero!=0:
            menor_numero=numero
    return menor_numero


def clasifica(string):
    lista=[]
    lista_pares = []
    lista_impar = []
    for i in string:
        contador=0
        for j in i:
            contador+=1
            if contador==11:
                if float(j)%2==0:
                    lista_pares.append(i)
                elif float(j)%2==1:
                    lista_impar.append(i)
    lista.append(lista_pares)
    lista.append(lista_impar)
    return lista


def palabras(string, numero):
    lista_string=string.split(" ")
    contador_palabras=0
    for i in lista_string:
        contador_letras=0
        for j in i:
            contador_letras+=1
        if contador_letras==numero:
            contador_palabras+=1
    return contador_palabras


def funcion_triangular(numero):
    lista=[]
    for i in range(0,numero):
        lista2=[]
        for j in range(0,numero):
            if i+1 > j:
                lista2.append(1)
            else:
                lista2.append(0)
        lista.append(lista2)
    return (lista)



def ganador():
    try:
        archivo=open("tiempos.csv", "r", encoding="UTF-8")
    except IOError:
        print("No encuntro el archivo")
    else:
        try:
            subir=open("tiempo_finales.txt", "w", encoding="UTF-8")
        except IOError:
            print("No se encontro el archivo :(")
        else:
            subir_string="Este archivo dice el tiempo total que cada corredor realizo y quien fue el ganador de la competencia\n"
            time = 100
            corredor_ganador=""
            for linea in archivo:
                sin_espacios = linea.rstrip()
                lista = sin_espacios.split(",")
                if lista[1]!="Tiempo1":
                    tiempo=(float(lista[1])+float(lista[2])+float(lista[3])+float(lista[4])+float(lista[5]))
                    if tiempo<time:
                        time=tiempo
                        corredor_ganador=lista[0]
                    subir_string+=(f"El corredor {lista[0]} realizo un tiempo de {tiempo:2.1f}\n")
            subir_string+=(f"El corredor que gano la competencia fue {corredor_ganador}, quien hizo el menor tiempo con {time}")
            subir.write(subir_string)
            subir.close()
            archivo.close()

#funcion menor ingresado
numero_pequeño=menor_ingresado()
print(f"El numero mas pequeño ingresado por el usuario fue {numero_pequeño:4.2f}")
print("\n")

#funcion pares e impares
string_clasifica=["X1222345688","T1255678991","Z3451231235","R0234556712","W9911234887"]
lista_par_impar=clasifica(string_clasifica)
for i in lista_par_impar:
    print(i)
print("\n")

#funcion contadora de letras en palabras
string_palabras="Un dia tendre una cabaña en Mazamitla"
numero_palabras=2
letras=palabras(string_palabras,numero_palabras)
print(f"La cantidad de palabras con {numero_palabras} letras  es {letras} en el string: {string_palabras}")
print("\n")

#funcion triagular
numero=2
lista_triangular=funcion_triangular(numero)
for i in lista_triangular:
    print(i)

#funcion archivos
ganador()


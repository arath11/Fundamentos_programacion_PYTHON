opcion=str(input("Este programa convierte cifras \n Para convertir de millas a km (1) \n La segunda de km a millas (2) \n Para convertir de pies a cm (3) \n Que opcion desea hacer?:"))
#cuando se escriba salir el programa se saldra, no correra más
while opcion!="salir":
    #compara el numero que escogio para hacer la conversiones y depues imprimirlas, en caso de ser un valor no valido le pedira que
    #lo vuelva a escrcibir como 4(no es valido en este programa )
    if opcion=="1":
        numero=float(input("Escriba el numero que quiere convertir de millas a km \n"))
        resultado=numero*1.60934
        print(numero, " millas, es igual a ", resultado, " kilometros")

    elif opcion=="2":
            numero=float(input("Escriba el numero que quiere convertir de km a millas \n"))
            resultado=numero/1.60934
            print(numero, " kilometros, es igual a ", resultado, " millas")
    elif opcion=="3":
            numero=float(input("Escriba el numero que quiere convertir de pies a cm\n"))
            resultado=numero*30.47992424196
            print(numero, " pies , es igual a ", resultado, " cm.")
    else:
        print(" \n--------------------- \nUsted escribio una opcion no valida, por favor escribala denuevo \n ------------------")
    opcion=str(input("\nAhora podras volver a hacer las conversiones \nPara convertir de millas a km (1) \n La segunda de km a millas (2) \n la tercera \n La tercera de pies a cm (3) \n para salir escriba (salir) \n Que opcion desea hacer?:"))

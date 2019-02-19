#Oscar Miranda A01630791
#Julio Arath Rosales Oliden A01630738


#Se pide que se ingrese el año
variable_1=float(input("Inserta el año, para checar si es un año bisiesto \n"))
#se compara si el año es multiplo de cuatro, despues se usa un or de divisible entre o 400 y un not de divisible entre 100, como es
#and dara falso si el año no es bisiesto lo que marcara como falsa o verdadero en caso de que sea bisiesto
if variable_1%4==0 and (not(variable_1%100==0) or variable_1%400==0 ):
    print("El año es bisiesto")
else:
    print("No es bisiesto")

#Comprendi mejor el uso de and, or y not. (aparte de que fue algo que vimos en mate discretas lo que nos ayudo)

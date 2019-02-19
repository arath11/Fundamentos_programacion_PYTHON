#Julio Arath Rosales
#A01630738
#Se pide la cantidad inicial
cantidad_inicial=float(input("Inserta la cantidad  \n"))
#Se divide la cantidad inicial sobre cien y se saca su residuo
cantidad_100=cantidad_inicial//100
restante_100=cantidad_inicial%100

cantidad_50=(restante_100//50)
#Se divide la cantidad anterior sobre cien y se saca su residuo
restante_50=(restante_100%50)

#Se divide la cantidad anterior sobre cien y se saca su residuo
cantidad_10=(restante_50//10)
restante_10=(restante_50%10)

#Se divide la cantidad anterior sobre cien y se saca su residuo
cantidad_5=(restante_10//5)
restante_5=(restante_10%5)

#Se divide la cantidad anterior sobre cien y se saca su residuo
cantidad_1=(restante_5//1)
restante_1=(restante_5%1)

print("El uso de billetes mas eficiente es \n %1.0f de 100" %(cantidad_100))
print("El uso de billetes mas eficiente es \n %1.0f de 50" %(cantidad_50))
print("El uso de billetes mas eficiente es \n %1.0f de 10" %(cantidad_10))
print("El uso de billetes mas eficiente es \n %1.0f de 5" %(cantidad_5))
print("El uso de billetes mas eficiente es \n %1.0f de 1" %(cantidad_1))

#Comprendi mejor el uso del residuo en esta actividad

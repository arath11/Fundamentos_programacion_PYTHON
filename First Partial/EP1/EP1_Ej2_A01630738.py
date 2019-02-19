#Se dice en que caso se dan los descuentos y se pide los datos de compra, tarjeta y cantidad de hijos
print("Hola, estamos en descuento..... \n Tienes tarjerta y 7 articulos o más te llevas 15 porciento de descuento \n Si no tienes tarjeta y 7 articulos o mas te llevas 10% \n o si tienes más de tres hijos te lelvas el descuento del 7 porciento")
cantidad=int(input("\n¿Cuantos productos compro?:"))
tarjeta=str(input("¿Tiene tarjeta (si/no):"))
hijos=int(input("¿Cuantos hijos tiene?:"))
precio_sin_des=cantidad*259.90

#Compararemos si compro 7 o mas articulo, y si tiene tarjeta o no con su descuento respectivo de 15% o 10%
#En caso de comprar menos de 7 articulos y tener más de 3 hijos se decunta 7%
#En caso de no cumplir cualquier requisito no se aplicara descuento
if cantidad>=7 and tarjeta=="si":
    precio=precio_sin_des*.85
    print("El precio sin descuento es de                   %10.2f $" %(precio_sin_des))
    print("El costo total de su compra con descuento es de %10.2f $" %(precio))
elif cantidad>=7 and tarjeta=="no":
    precio=precio_sin_des*.90
    print("El precio sin descuento es de                   %10.2f $" %(precio_sin_des))
    print("El costo total de su compra con descuento es de %10.2f $" %(precio))
elif cantidad<7 and hijos>3:
    precio=precio_sin_des*.93
    print("El precio sin descuento es de                   %10.2f $" %(precio_sin_des))
    print("El costo total de su compra con descuento es de %10.2f $" %(precio))
else:
    print("El costo total de su compra sin descuento  es de %10.2f $" %(precio_sin_des))

print("\n------------------------------------\nGracias por comprar con nosotros :)\n------------------------------------")

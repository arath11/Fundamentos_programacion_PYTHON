#Oscar Miranda A01630791
#Julio Arath Rosales Oliden A01630738

#Se pide el peso del producto
num=float(input("Dame el peso del producto \n"))
#Se compara en que rango de peso entra para despues hacer una pequeña ecuacion para asignar el precio del envio
if num <10:
  print("El costo del envio sera de 1200")
elif num>=10 and num<45:
  x=1200+(85*(num-10))
  print("El costo del envio sera de ", x)
elif num>=45 and num<=90:
  x=2700+(65*(num-25))
  print("El costo del envio sera de ", x)
elif num>90:
  x=3700+(75*(num-90))
  print("El costo del envio sera de ", x)

#Este programa nos ayudo a comprender mejor el elif

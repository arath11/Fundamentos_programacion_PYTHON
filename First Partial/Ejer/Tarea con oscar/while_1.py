
i=1
par=0
imp=0
while i<=10:
  num=int(input("Inserta el numero \n"))
  i+=1
  if num%2==0:
      par+=1
  elif num%1==0:
      imp+=1


print("Fueron ", str(par), " numeros pares y ", str(imp), " impares")

import math

pi=math.pi
print("4(pi)r**r")
radio=int(input("Escribe el radio"))
mate1=float(1)
mate1=radio*radio
mate1=mate1*pi
mate1=mate1*4
print(mate1)

print("Sacaremos la distancia entre dos puntos, por favor pon los datos requeridos")
x2=int(input("Escribe la cordenada x2"))
x1=float(input("Escribe la cordenada x1"))
y2=float(input("Escribe la cordenada y2"))
y1=float(input("Escribe la cordenada y1"))
ar=(((x2-x1)**2)+((y2-y1)**2))
mate2=math.sqrt(ar)
print(mate2)
print("La distancia entre los puntos introducidos es " + str(mate2))
print("La distancia %2.3f" %(mate2))
print("la distancia {0:2.5f} " .format(mate2))

print("inserta los datos a y b")
a=float(input("inserta a"))
b=float(input("inserta b"))
mate3=float(1)
mate3=(a+b)*(a+b)
mate3=(mate3*(2**2))
mate3=math.sqrt(mate3)
mate3=math.pi*mate3
print(mate3)

print("inserta los siguientes valores")
x=float(input("insterta x"))
y=float(input("inserta y"))
a=float(input("inserta a"))
b=float(input("inserta b"))
mate5=b/(2*a)
mate5=mate5*(x-y)
print(mate5)


print("insterta los siguientes valores")
x=float(input("inserta x"))
y=float(input("inserta y"))
a=float(input("inserta a"))
b=float(input("inserta b"))
mate4=x*x
mate4=mate4/(a+b)
mate4=mate4/(x*y)
mate4=mate4*(a**2)
print(mate4)

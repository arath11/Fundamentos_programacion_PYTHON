import math
def cuadrado(x):
    resultado=x**2
    return resultado
def saludo_1():
    print("buenos dias")
def saludo_2(nombre):
    print(f"Buenos dias, {nombre} ")

def suma(x, y):
    return x + y

numero=12
print(f"El numero al cuadrado es {cuadrado(numero):5d} ")
#result=cuadrado(25)
print(cuadrado(25))
#print(result)

saludo_1()
saludo_2("Oscar")


print(suma(1, 2))




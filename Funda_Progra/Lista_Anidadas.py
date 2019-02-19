#Validacion de enteros
def valida_entero(msg):
    while True:
        dato=input(msg)
        try:
            valor=int(dato)
        except ValueError:
            print("Dato invalido")
        else:
            return valor

def valida_rango(msg):
    while True:
        dato=input(msg)
        try:
            valor=int(dato)
        except ValueError:
            print("Dato invalido")
        else:
            if 100 >= valor and valor >= 0:
                return valor
            else:
                print("Dato fuera de rango ")



numero=valida_rango("Ingresa numero:")
print(f"El dato tecleado fue {numero}")

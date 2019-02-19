#Julio Arath Rosales Oliden
#A0160378
#Se crea una lista ya existente de la cual se modificaran los datos
lista=["abc", "julio", "oscar", "Lista", "hola mundo"]
#Se imprime la lista anteirior y un espacio entre la nueva para que se vea mejor
print(f" La  lista anterior era {lista}")
print("\n-----------------------------------------------------------------------\n")
#Por la cantidad de datos en la lista se realizara
for i in range(len(lista)):
    # una busqueda en la posicion i de la lista para cambiar la palabra a la misma pero ahora con mayusculas
    lista[i]=lista[i].upper()
print(f" La nueva lista es {lista}")
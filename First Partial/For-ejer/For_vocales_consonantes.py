palabra=input("Escribe una palabra")
vocales=[]
consonantes=[]

for letra in palabra:
    if letra in "aeiouAEIOU":
        vocales.append(letra)
    else:
        consonantes.append(letra)
vocal="".join(vocales)
consonante="".join(consonantes)
print(f"Nos quedan las palabras: {vocal} y {consonante} ")
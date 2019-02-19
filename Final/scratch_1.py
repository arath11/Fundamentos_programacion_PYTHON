print("")

a = float(input("¿Cuál es el valor de a?"))
b = float(input("¿Cuál es el valor de b?"))
c = float(input("¿Cuál es el valor de c?"))

#A partir de los valores obtenidos, con las formulas correspondientes sacar perímetro (P), la variable s y finalmente el área (A)

P = a + b + c
S = P / 2
A = ( (S * (S - a)) * (S - b) * (S - c)) ** (1 / 2 )

# Mostrar al usuario el valor de Perímetro y Área

print(f"El triángulo con lado a= {a}, lado b= {b} y lado c= {c}. Tiene un perímetro de: {P: .2f} y un área de: {A:.2f}")
#pide el sueldo
sueldo=float(input("Inserta el sueldo  \n"))

descuento=0
#verifica que sea mayor que 100
if sueldo>100:
    #compara para saber en que rango entra, para despues hacer la resta del sueldo menos descuento
    if sueldo>1000 and sueldo<=2500:
        descuento=67.30+(sueldo*.12)
        sueldo=sueldo-descuento
        print("Del sueldo se descuento", descuento)
        print("Y el sueldo final es de", sueldo)

    elif sueldo>2500:
        descuento=211.20+(sueldo*.23)
        sueldo=sueldo-descuento
        print("Del sueldo se descuento", descuento)
        print("Y el sueldo final es de", sueldo)
    elif sueldo<=1000:
        descuento=34.50+(sueldo*.035)
        sueldo=sueldo-descuento
        print("Del sueldo se descuento", descuento)
        print("Y el sueldo final es de", sueldo)


else:
    print("la cantidad insertada es no valida, ya que el sueldo menor de esta empresa es 100")
#aprendi a usar if anidados

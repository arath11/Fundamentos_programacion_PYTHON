numero_1=float(input("Dame el numero inferior "))
numero_2=float(input("dameel lnuemro superior"))

cantidad_pasos=((numero_2-numero_1)/2)-1
#print(cantidad_pasos)
imprimir=numero_1+2
while cantidad_pasos>=0:
    print(imprimir)
    imprimir+=2
    cantidad_pasos-=1

factorial=float(input("factkorial"))
multi=0
n=1
x=1

while (factorial!=0 or factorial!=1) and (factorial>-1) and factorial>=x:
    print(x)
    x*=n
    n+=1


multi=float(input("insetre un numero"))
n=1
while 10>=n:
    resultado=multi*n
    print(multi, "x", n, "=", resultado)
    n+=1

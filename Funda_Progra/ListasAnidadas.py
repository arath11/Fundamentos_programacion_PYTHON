lista=[1,2,3,4,5]
listaA=[[1,2,3],[4,5,6],[7,8,9]]
print(listaA[2][1])


for i in range(len(listaA)):
    for a in range(len(listaA[i])):
        print(listaA[i][a])

def cuentaPares(lista):
    pares=0
    for i in range(len(listaA)):
        for a in range(len(listaA[i])):
            if listaA[i][a]%2==0:
                pares+=1
    return pares
print(cuentaPares(listaA))


lista1_m=[[1,2],[3,4],[5,6]]
lista2_m=[[7,8],[9,10],[11,12]]
lista3=[[0,0],[0,0],[0,0]]
for a in range(len(lista1_m)):
    for b in range(len(lista1_m[a])):
        lista3[a][b]=lista1_m[a][b]+lista2_m[a][b]
print(lista3)
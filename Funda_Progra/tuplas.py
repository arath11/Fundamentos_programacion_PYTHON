lista1=[[1,2,3], [7,6,5], [0,0,1]]
lista2=[[1,2,3], [7,6,5], [0,0,1]]
lista3=[[0,0,0], [0,0,0], [0,0,0]]
def __parte1__():
    for i in range(len(lista1)):
        print("------1")
        for a in range(len(lista1)):
            print("----2")
            for w in range(len(lista2)):
               print("---3")
               for q in range(len(lista2)):
                    print("--4")
                    print(lista1[i][a], lista2[w][a])
                    lista3[i][a]=lista1[i][a]*lista2[w][q]
                    print(lista3)

__parte1__()


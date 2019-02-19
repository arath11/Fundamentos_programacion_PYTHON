def __x__(n):
    lista1 = []
    lista2 = []
    lista_numbers = []

    sum1=1
    y=1
    compare=n-1
    while y<n:
        if n%y==0 :
            if y!=1:
                lista1.append(y)
        y+=1
    print(lista1)

    while compare!=0:
        y = 1
        while y < (compare+1):
            if compare%y == 0:
                if y!=1:
                    lista2.append(y)
            y += 1
        for i in range(len(lista1)):
            for a in range(len(lista2)):
                p=(len(lista2)-1)
                if lista1[i]!=lista2[a]:
                    lista_numbers.append(lista2[p])
        lista2.append(compare)
      #  print(lista2)
        lista2=[]
     #   print(lista2)
        compare-=1
    print(lista_numbers)
    return len(lista_numbers)

num=float(input("Please give the number:\n"))
a=__x__(num)
print(a)





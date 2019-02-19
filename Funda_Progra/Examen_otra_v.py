


def anagramas(palabra1,palabra2):
    if len(palabra1) == len(palabra2)  and (palabra1 != palabra2):
        for letra in palabra1:
            if letra not in palabra2:
                return False
        return True
    else:
        return False

def cambia_multplos(lista, n):
    for pos in range(len(lista)):
        if lista[pos]%n==0:
            lista[pos]=0
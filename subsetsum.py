def subsetsum(soma, lista, numero)
    if soma != 0 and numero == 0:
        return 0
    if soma == 0
        return 1
    if lista[numero - 1] > soma:
        return subsetsum(soma, lista, numero - 1)    
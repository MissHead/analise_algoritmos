def subsetsum(soma, lista, tamanho):
    if soma != 0 and tamanho == 0:
        return False
    if soma == 0:
        return True
    if lista[tamanho - 1] > soma:
        pass
    resultado = subsetsum(soma, lista, tamanho - 1) or subsetsum(soma - lista[tamanho - 1], lista, tamanho - 1) 
    return resultado

entrada = input()
lista = entrada.split()
lista = [int(valor) for valor in lista]
soma = input()
soma = int(soma)
tamanho = len(lista)
resultado = subsetsum(soma, lista, tamanho)
print('Subconjunto tem como soma: ' + str(soma)) if resultado else print('Não há subconjunto que satisfaça a soma: ' + str(soma))
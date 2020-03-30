def subsetsum(soma, lista, tamanho):
    if soma != 0 and tamanho == 0:
        return 0
    if soma == 0:
        return 1
    if lista[tamanho - 1] > soma:
        return subsetsum(soma, lista, tamanho - 1) 

entrada = input()
lista = entrada.split()
lista = [int(valor) for valor in lista]
soma = input()
soma = int(soma)
tamanho = len(lista)
subsetsum(soma, lista, tamanho)
print(lista, soma, tamanho)
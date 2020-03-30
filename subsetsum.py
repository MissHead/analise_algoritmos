def subsetsum(soma, conjunto, tamanho):
    if soma != 0 and tamanho == 0:
        return False
    if soma == 0:
        return True
    if conjunto[tamanho - 1] > soma:
        pass
    resultado = subsetsum(soma, conjunto, tamanho - 1) or subsetsum(soma - conjunto[tamanho - 1], conjunto, tamanho - 1) 
    return resultado

entrada = input()
conjunto = entrada.split()
conjunto = [int(valor) for valor in conjunto]
soma = input()
soma = int(soma)
tamanho = len(conjunto)
resultado = subsetsum(soma, conjunto, tamanho)
print('Subconjunto tem como soma: ' + str(soma)) if resultado else print('Não há subconjunto que satisfaça a soma: ' + str(soma))
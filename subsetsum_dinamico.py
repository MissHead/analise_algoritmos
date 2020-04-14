import numpy

def subsetsum_tabela(soma, tamanho, conjunto):
    tabela = numpy.zeros(soma + 1, dtype=numpy.int32)
    for i in range(0, tamanho):
        for j in range(soma - conjunto[i], -1, -1):
            if (j == 0):
                if (tabela[conjunto[i]] == 0):
                    tabela[conjunto[i]] = conjunto[i]
            elif (tabela[j] != 0 and tabela[j+conjunto[i]] == 0):
                tabela[j+conjunto[i]] = conjunto[i]
    return tabela

def converte_subconjunto(soma, tabela):
    indice = []
    tamanho = 0
    i = soma
    while (0 < i):
        indice.append(tabela[i])
        i = i - tabela[i]
        tamanho = tamanho + 1
    return tamanho, indice

conjunto = numpy.array([int(elementos) for elementos in input().split()])
soma = int(input())
tamanho = len(conjunto)
tabela = subsetsum_tabela(soma, tamanho, conjunto)

if (tabela[soma] == 0):
    print('Não há subconjunto que satisfaça a soma: ' + str(soma))
else:
    maior_indice, lista = converte_subconjunto(soma, tabela)
    print('Subconjunto =')
    for i in range(0, maior_indice):
        if 0 < i:
            print('+')
        print('%d' % (lista[i]))
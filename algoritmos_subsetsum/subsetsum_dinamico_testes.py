import numpy, time

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

print('Tempo Execução para SubsetSum Dinâmico\n')
#01
conjunto = numpy.array([2, 5, 7, 8, 10, 12])
soma = 17
tamanho = len(conjunto)
inicio = time.time()
subsetsum_tabela(soma, tamanho, conjunto)
fim = time.time()
print(str(fim-inicio).replace('.',','))
#02
conjunto = numpy.array([5, 10, 15, 20, 25, 30, 35])
soma = 50
tamanho = len(conjunto)
inicio = time.time()
subsetsum_tabela(soma, tamanho, conjunto)
fim = time.time()
print(str(fim-inicio).replace('.',','))
#03
conjunto = numpy.array([3, 5, 7, 9, 11, 13, 21, 33])
soma = 36
tamanho = len(conjunto)
inicio = time.time()
subsetsum_tabela(soma, tamanho, conjunto)
fim = time.time()
print(str(fim-inicio).replace('.',','))
#04
conjunto = numpy.array([4, 6, 8, 10, 12, 16, 18, 22, 26, 32])
soma = 40
tamanho = len(conjunto)
inicio = time.time()
subsetsum_tabela(soma, tamanho, conjunto)
fim = time.time()
print(str(fim-inicio).replace('.',','))
#05
conjunto = numpy.array([10, 12, 22, 27, 31, 39, 46, 48, 50, 59])
soma = 90
tamanho = len(conjunto)
inicio = time.time()
subsetsum_tabela(soma, tamanho, conjunto)
fim = time.time()
print(str(fim-inicio).replace('.',','))
#06
conjunto = numpy.array([1, 3, 12, 15, 20, 22, 27, 30, 32, 45, 48, 51, 55, 59, 66])
soma = 100
tamanho = len(conjunto)
inicio = time.time()
subsetsum_tabela(soma, tamanho, conjunto)
fim = time.time()
print(str(fim-inicio).replace('.',','))
#07
conjunto = numpy.array([2, 4, 12, 14, 20, 24, 30, 44, 66, 98, 102, 110, 200, 300, 450, 500])
soma = 534
tamanho = len(conjunto)
inicio = time.time()
subsetsum_tabela(soma, tamanho, conjunto)
fim = time.time()
print(str(fim-inicio).replace('.',','))
#08
conjunto = numpy.array([90, 100, 150, 234, 257, 342, 403, 433, 591, 600, 762, 799, 800, 821, 853, 876, 901])
soma = 1390
tamanho = len(conjunto)
inicio = time.time()
subsetsum_tabela(soma, tamanho, conjunto)
fim = time.time()
print(str(fim-inicio).replace('.',','))
#09
conjunto = numpy.array([3, 6, 9, 12, 13, 18, 19, 23, 24, 30, 33, 36, 40, 42, 43, 48, 54, 60, 150, 200, 333, 400, 500, 666])
soma = 6666
tamanho = len(conjunto)
inicio = time.time()
subsetsum_tabela(soma, tamanho, conjunto)
fim = time.time()
print(str(fim-inicio).replace('.',','))
import numpy, time

def busca_ultimo_1(tamanho, subconjunto, indice):
    maior_indice = -1
    for i in range (indice - 1, -1, -1):
        if (subconjunto[i] == 1):
            maior_indice = i
            break
    return maior_indice

def subconjunto_produz_soma(soma, tamanho, conjunto, produz, subconjunto, maior_indice):
    if not produz:
        maior_indice = -1
        subconjunto = numpy.zeros(tamanho)
    else:
        produz = False
        subconjunto[maior_indice] = 0
        maior_indice = busca_ultimo_1(tamanho, subconjunto, maior_indice)
        if maior_indice < 0:
            return produz, subconjunto, maior_indice
        subconjunto[maior_indice] = 0
        maior_indice = maior_indice + 1
        subconjunto[maior_indice] = 1
    while True:
        produto = numpy.dot(subconjunto, conjunto)
        if produto < soma and maior_indice < tamanho - 1:
            maior_indice = maior_indice + 1
            subconjunto[maior_indice] = 1
        else:
            if produto == soma:
                produz = True
                return produz, subconjunto, maior_indice
            subconjunto[maior_indice] = 0
            maior_indice = busca_ultimo_1(tamanho, subconjunto, maior_indice)
            if maior_indice < 0:
                break
            subconjunto[maior_indice] = 0
            maior_indice = maior_indice + 1
            subconjunto[maior_indice] = 1
    return produz, subconjunto, maior_indice

print('Tempo Execução para SubsetSum Backtracking\n')
#01
conjunto = numpy.array([2, 5, 7, 8, 10, 12])
soma = 17
tamanho = len(conjunto)
subconjunto = numpy.zeros(tamanho)
produz = False
maior_indice = 0
inicio = time.time()
while True:
    produz, subconjunto, maior_indice = subconjunto_produz_soma(soma, tamanho, conjunto, produz, subconjunto, maior_indice)
    if ( not produz ):
        break
fim = time.time()
print(str(fim-inicio).replace('.',','))
#02
conjunto = numpy.array([2, 5, 7, 8, 10, 12])
soma = 17
tamanho = len(conjunto)
subconjunto = numpy.zeros(tamanho)
produz = False
maior_indice = 0
inicio = time.time()
while True:
    produz, subconjunto, maior_indice = subconjunto_produz_soma(soma, tamanho, conjunto, produz, subconjunto, maior_indice)
    if ( not produz ):
        break
fim = time.time()
print(str(fim-inicio).replace('.',','))
#03
conjunto = numpy.array([3, 5, 7, 9, 11, 13, 21, 33])
soma = 36
tamanho = len(conjunto)
subconjunto = numpy.zeros(tamanho)
produz = False
maior_indice = 0
inicio = time.time()
while True:
    produz, subconjunto, maior_indice = subconjunto_produz_soma(soma, tamanho, conjunto, produz, subconjunto, maior_indice)
    if ( not produz ):
        break
fim = time.time()
print(str(fim-inicio).replace('.',','))
#04
conjunto = numpy.array([4, 6, 8, 10, 12, 16, 18, 22, 26, 32])
soma = 40
tamanho = len(conjunto)
subconjunto = numpy.zeros(tamanho)
produz = False
maior_indice = 0
inicio = time.time()
while True:
    produz, subconjunto, maior_indice = subconjunto_produz_soma(soma, tamanho, conjunto, produz, subconjunto, maior_indice)
    if ( not produz ):
        break
fim = time.time()
print(str(fim-inicio).replace('.',','))
#05
conjunto = numpy.array([10, 12, 22, 27, 31, 39, 46, 48, 50, 59])
soma = 90
tamanho = len(conjunto)
subconjunto = numpy.zeros(tamanho)
produz = False
maior_indice = 0
inicio = time.time()
while True:
    produz, subconjunto, maior_indice = subconjunto_produz_soma(soma, tamanho, conjunto, produz, subconjunto, maior_indice)
    if ( not produz ):
        break
fim = time.time()
print(str(fim-inicio).replace('.',','))
#06
conjunto = numpy.array([1, 3, 12, 15, 20, 22, 27, 30, 32, 45, 48, 51, 55, 59, 66])
soma = 100
tamanho = len(conjunto)
subconjunto = numpy.zeros(tamanho)
produz = False
maior_indice = 0
inicio = time.time()
while True:
    produz, subconjunto, maior_indice = subconjunto_produz_soma(soma, tamanho, conjunto, produz, subconjunto, maior_indice)
    if ( not produz ):
        break
fim = time.time()
print(str(fim-inicio).replace('.',','))
#07
conjunto = numpy.array([2, 4, 12, 14, 20, 24, 30, 44, 66, 98, 102, 110, 200, 300, 450, 500])
soma = 534
tamanho = len(conjunto)
subconjunto = numpy.zeros(tamanho)
produz = False
maior_indice = 0
inicio = time.time()
while True:
    produz, subconjunto, maior_indice = subconjunto_produz_soma(soma, tamanho, conjunto, produz, subconjunto, maior_indice)
    if ( not produz ):
        break
fim = time.time()
print(str(fim-inicio).replace('.',','))
#08
conjunto = numpy.array([90, 100, 150, 234, 257, 342, 403, 433, 591, 600, 762, 799, 800, 821, 853, 876, 901])
soma = 1390
tamanho = len(conjunto)
subconjunto = numpy.zeros(tamanho)
produz = False
maior_indice = 0
inicio = time.time()
while True:
    produz, subconjunto, maior_indice = subconjunto_produz_soma(soma, tamanho, conjunto, produz, subconjunto, maior_indice)
    if ( not produz ):
        break
fim = time.time()
print(str(fim-inicio).replace('.',','))
#09
conjunto = numpy.array([3, 6, 9, 12, 13, 18, 19, 23, 24, 30, 33, 36, 40, 42, 43, 48, 54, 60, 150, 200, 333, 400, 500, 666])
soma = 6666
tamanho = len(conjunto)
subconjunto = numpy.zeros(tamanho)
produz = False
maior_indice = 0
inicio = time.time()
while True:
    produz, subconjunto, maior_indice = subconjunto_produz_soma(soma, tamanho, conjunto, produz, subconjunto, maior_indice)
    if ( not produz ):
        break
fim = time.time()
print(str(fim-inicio).replace('.',','))
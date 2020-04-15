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
#01 subconjunto produz a soma:
conjunto = [1, 2, 3, 4, 5]
soma = 1
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

#02 subconjuntos produzem a soma:
conjunto = [12, 16, 18, 22, 24, 28]
soma = 34
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

#03 subconjuntos produzem a soma:
conjunto = [10, 12, 22, 27, 31, 39, 46, 48, 50, 59]
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

#04 subconjuntos produzem a soma:
conjunto = [2, 5, 7, 8, 10, 12]
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

#05 subconjuntos produzem a soma:
conjunto = [3, 5, 7, 9, 11, 13, 21, 31, 33]
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

#10 subconjuntos produzem a soma:
conjunto = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
soma = 50
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

#15 subconjuntos produzem a soma:
conjunto = [4, 6, 8, 10, 12, 16, 18, 22, 26, 32, 40]
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

#20 subconjuntos produzem a soma:
conjunto = [2, 3, 6, 9, 13, 15, 17, 29, 34, 42, 51, 53, 59]
soma = 68
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

#30 subconjuntos produzem a soma:
conjunto = [1, 3, 12, 15, 20, 22, 27, 30, 32, 45, 48, 51, 55, 59, 66]
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

#55 subconjuntos produzem a soma:
conjunto = [4, 5, 7, 8, 12, 14, 16, 17, 23, 25, 26, 27, 29, 34, 36, 40, 60]
soma = 60
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

#70 subconjuntos produzem a soma:
conjunto = [5, 6, 14, 16, 17, 20, 23, 25, 26, 27, 29, 30, 34, 36, 40, 46, 58, 60, 62, 64, 66, 68]
soma = 86
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

#195 subconjuntos produzem a soma:
conjunto = [5, 10, 12, 14, 16, 17, 20, 23, 25, 26, 27, 29, 30, 34, 36, 40, 46, 58, 60, 62, 64, 66, 68, 70, 75, 76]
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

#275 subconjuntos produzem a soma:
conjunto = [15, 21, 39, 45, 50, 61, 73, 85, 90, 100, 150, 234, 257, 342, 403, 433, 591, 600, 762, 799, 800, 821, 853, 876, 901]
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

#315 subconjuntos produzem a soma:
conjunto = [1, 3, 5, 7, 8, 9, 10, 13, 19, 23, 31, 43, 51, 54, 63, 65, 70, 76, 82, 87, 98, 100, 123]
soma = 123
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

#515 subconjuntos produzem a soma:
conjunto = [1, 2, 3, 4, 12, 14, 20, 21, 24, 30, 34, 44, 66, 98, 102, 110, 200, 300, 450, 500, 534]
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

#2215
conjunto = [5, 7, 10, 15, 21, 39, 45, 50, 61, 73, 85, 90, 100, 150, 234, 257, 342, 403, 433, 591, 600, 762, 799, 800, 821, 853, 876, 901]
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

#5490 subconjuntos produzem a soma:
conjunto = [3, 6, 9, 12, 13, 18, 19, 23, 24, 30, 33, 36, 40, 42, 43, 48, 54, 60, 150, 200, 333, 400, 500, 666]
soma = 666
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
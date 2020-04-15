import numpy

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

conjunto = numpy.array([int(elementos) for elementos in input().split()])
soma = int(input())
tamanho = len(conjunto)
subconjunto = numpy.zeros(tamanho)
produz = False
maior_indice = 0
k = 0
while True:
    produz, subconjunto, maior_indice = subconjunto_produz_soma(soma, tamanho, conjunto, produz, subconjunto, maior_indice)
    if ( not produz ):
        break
    k = k + 1
    print('Subconjunto %d = ' % (k)),
    plus = False
    for i in range(0, tamanho):
        if subconjunto[i] != 0:
            if ( plus ):
                print ( '+' ),
            print ('%d' % (conjunto[i])),
            plus = True
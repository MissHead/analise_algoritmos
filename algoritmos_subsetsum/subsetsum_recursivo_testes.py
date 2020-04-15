import time
def subsetsum(soma, conjunto):
    if soma == 0:
        return False
    elif len(conjunto) == 0:
        return False
    else:
        if conjunto[0] == soma:
            return [conjunto[0]]
        else:
            subconjunto = subsetsum((soma - conjunto[0]), conjunto[1:]) 
            if subconjunto:
                return [conjunto[0]] + subconjunto
            else:
                return subsetsum(soma, conjunto[1:])
                
print('Tempo Execução para SubsetSum Recursivo\n')
#01
conjunto = [2, 5, 7, 8, 10, 12]
soma = 17
inicio = time.time()
subsetsum(soma, conjunto)
fim = time.time()
print(str(fim-inicio).replace('.',','))
#02
conjunto = [5, 10, 15, 20, 25, 30, 35]
soma = 50
inicio = time.time()
subsetsum(soma, conjunto)
fim = time.time()
print(str(fim-inicio).replace('.',','))
#03
conjunto = [3, 5, 7, 9, 11, 13, 21, 33]
soma = 36
inicio = time.time()
subsetsum(soma, conjunto)
fim = time.time()
print(str(fim-inicio).replace('.',','))
#04
conjunto = [4, 6, 8, 10, 12, 16, 18, 22, 26, 32]
soma = 40
inicio = time.time()
subsetsum(soma, conjunto)
fim = time.time()
print(str(fim-inicio).replace('.',','))
#05
conjunto = [10, 12, 22, 27, 31, 39, 46, 48, 50, 59]
soma = 90
inicio = time.time()
subsetsum(soma, conjunto)
fim = time.time()
print(str(fim-inicio).replace('.',',')) 
#06
conjunto = [1, 3, 12, 15, 20, 22, 27, 30, 32, 45, 48, 51, 55, 59, 66]
soma = 100
inicio = time.time()
subsetsum(soma, conjunto)
fim = time.time()
print(str(fim-inicio).replace('.',','))
#07
conjunto = [2, 4, 12, 14, 20, 24, 30, 44, 66, 98, 102, 110, 200, 300, 450, 500]
soma = 534
inicio = time.time()
subsetsum(soma, conjunto)
fim = time.time()
print(str(fim-inicio).replace('.',','))
#08
conjunto = [90, 100, 150, 234, 257, 342, 403, 433, 591, 600, 762, 799, 800, 821, 853, 876, 901]
soma = 1390
inicio = time.time()
subsetsum(soma, conjunto)
fim = time.time()
print(str(fim-inicio).replace('.',','))
#09
conjunto = [3, 6, 9, 12, 13, 18, 19, 23, 24, 30, 33, 36, 40, 42, 43, 48, 54, 60, 150, 200, 333, 400, 500, 666]
soma = 6666
inicio = time.time()
subsetsum(soma, conjunto)
fim = time.time()
print(str(fim-inicio).replace('.',','))
def subsetsum(soma, conjunto):
    if soma == 0 or soma < 1:
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
    
entrada = input()
conjunto = entrada.split()
conjunto = [int(valor) for valor in conjunto]
soma = input()
soma = int(soma)
tamanho = len(conjunto)
resultado = subsetsum(soma, conjunto)
print('O Subconjunto: ' + str(resultado) + ' tem como soma: ' + str(soma)) if resultado else print('Não há subconjunto que satisfaça a soma: ' + str(soma))
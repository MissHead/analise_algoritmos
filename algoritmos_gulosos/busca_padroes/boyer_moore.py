import string

def sufixos_lista(palavra):
    assert len(palavra) > 1
    sufixo = [len(palavra)] + [0] * (len(palavra)-1)
    for i in range(1, len(palavra)):
        if palavra[i] == palavra[i-1]:
            sufixo[1] += 1
        else:
            break
    direita, esquerda = 0, 0
    if sufixo[1] > 0:
        direita, esquerda = sufixo[1], 1
    for k in range(2, len(palavra)):
        assert sufixo[k] == 0
        if k > direita:
            for i in range(k, len(palavra)):
                if palavra[i] == palavra[i-k]:
                    sufixo[k] += 1
                else:
                    break
            direita, esquerda = k + sufixo[k] - 1, k
        else:
            prefixo_palavra = direita - k + 1
            sufixo_palavra = sufixo[k - esquerda]
            if prefixo_palavra > sufixo_palavra:
                sufixo[k] = sufixo_palavra
            else:
                nmatch = 0
                for i in range(direita+1, len(palavra)):
                    if palavra[i] == palavra[i - k]:
                        nmatch += 1
                    else:
                        break
                esquerda, direita = k, direita + nmatch
                sufixo[k] = direita - k + 1
    return sufixo

def constroi_sequencia(palavra):
    return sufixos_lista(palavra[::-1])[::-1]

def maior_sequenciap(palavra, n):
    maior = [0] * len(palavra)
    for j in range(len(palavra)-1):
        i = len(palavra) - n[j]
        if i < len(palavra):
            maior[i] = j + 1
    return maior

def sequencia_principal(palavra, lp):
    l = [0] * len(palavra)
    l[1] = lp[1]
    for i in range(2, len(palavra)):
        l[i] = max(l[i-1], lp[i])
    return l

def menor_sequenciap(n):
    menor = [0] * len(n)
    for i in range(len(n)):
        if n[i] == i+1:  
            menor[len(n)-i-1] = i+1
    for i in range(len(n)-2, -1, -1): 
        if menor[i] == 0:
            menor[i] = menor[i+1]
    return menor

def tabela_melhor_sufixo(palavra):
    n = constroi_sequencia(palavra)
    lp = maior_sequenciap(palavra, n)
    return lp, sequencia_principal(palavra, lp), menor_sequenciap(n)

def nao_tem_sufixo(i, maior, menor):
    tamanho = len(maior)
    assert i < tamanho
    if i == tamanho - 1:
        return 0
    i += 1  
    if maior[i] > 0:
        return tamanho - maior[i]
    return tamanho - menor[i]

def tem_sufixo(menor):
    return len(menor) - menor[1]

def tabela_pior_caractere(palavra, mapa):
    tab = []
    nxt = [0] * len(mapa)
    for i in range(0, len(palavra)):
        c = palavra[i]
        assert c in mapa
        tab.append(nxt[:])
        nxt[mapa[c]] = i+1
    return tab

class BoyerMoore(object):
    
    def __init__(self, palavra, alfabeto):
        self.palavra = palavra
        self.alfabeto = alfabeto
        self.mapa = {}
        for i in range(len(self.alfabeto)):
            self.mapa[self.alfabeto[i]] = i
        self.pior_caractere = tabela_pior_caractere(palavra, self.mapa)
        _, self.maior_sequencia, self.menor = tabela_melhor_sufixo(palavra)
    
    def regraPiorCaractere(self, i, c):
        assert c in self.mapa
        ci = self.mapa[c]
        assert i > (self.pior_caractere[i][ci]-1)
        return i - (self.pior_caractere[i][ci]-1)
    
    def regraMelhorSufixo(self, i):
        tamanho = len(self.maior_sequencia)
        assert i < tamanho
        if i == tamanho - 1:
            return 0
        i += 1 
        if self.maior_sequencia[i] > 0:
            return tamanho - self.maior_sequencia[i]
        return tamanho - self.menor[i]
    
    def excessao(self):
        return len(self.menor) - self.menor[1]

def boyer_moore(palavra, BM, texto):
    i = 0
    ocorrencias = []
    while i < len(texto) - len(palavra) + 1:
        avanca = 1
        nao_tem = False
        for j in range(len(palavra)-1, -1, -1):
            if palavra[j] != texto[i+j]:
                excessao_pior_caractere = BM.regraPiorCaractere(j, texto[i+j])
                excessao_melhor_sufixo = BM.regraMelhorSufixo(j)
                avanca = max(avanca, excessao_pior_caractere, excessao_melhor_sufixo)
                nao_tem = True
                break
        if not nao_tem:
            ocorrencias.append(i)
            excessao_melhor_sufixo = BM.excessao()
            avanca = max(avanca, excessao_melhor_sufixo)
        i += avanca
    return ocorrencias


texto = 'aaaccbabacabacbacbbcbbacababbbaacababcbcbcbbcbbbcbbacabababcbabcbccccbababcabb'
palavra = 'acaba'
BM = BoyerMoore(palavra, alfabeto='abc')
print(boyer_moore(palavra, BM, texto))
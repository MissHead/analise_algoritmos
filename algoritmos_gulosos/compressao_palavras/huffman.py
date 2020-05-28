import random, string, time, heapq
from collections import Counter

def palavraAleatoria(stringLength):
    letras = string.ascii_lowercase
    return ''.join(random.choice(letras) for i in range(stringLength))

def compressao(string):
    res = ""
    contador = 1
    res += string[0]
    for i in range(len(string)-1):
        if(string[i] == string[i+1]):
            contador+=1
        else:
            if(contador > 1):
                res += str(contador)
            res += string[i+1]
            contador = 1
    if(contador > 1):
        res += str(contador)
    return res

def probabilidades(conteudo):
    total = len(conteudo) + 1
    c = Counter(conteudo)
    res = {}
    for char,contador in c.items():
        res[char] = float(contador)/total
    res['end'] = 1.0/total
    return res

def constroiArvore(probabilidade):
    q = []
    for ch,pr in probabilidade.items():
        heapq.heappush(q,(pr,0,ch))
    while len(q) > 1:
        e1 = heapq.heappop(q)
        e2 = heapq.heappop(q)
        nw_e = (e1[0]+e2[0],max(e1[1],e2[1])+1,[e1,e2])
        heapq.heappush(q,nw_e)
    return q[0]

def constroiDicionario(arvore):
    res = {}
    pilha = []
    prefixo = ""
    pilha.append(arvore+("",)) 
    while len(pilha) > 0:
        elm = pilha.pop()
        if type(elm[2]) == list:
            pilha.append(elm[2][1]+(prefixo+"0",))
            pilha.append(elm[2][0]+(prefixo+"1",))
            continue
        else:
            code = elm[-1]
            res[elm[2]] = code
        pass
    return res

def huffman(dicionario,conteudo):
    res = ""
    for ch in conteudo:
        code = dicionario[ch]
        res = res + code
    res = '1' + res + dicionario['end']
    res = res + (len(res) % 8 * "0")
    return int(res,2)


tamanho_palavra = int(input())
palavra = palavraAleatoria(tamanho_palavra)
inicio = time.time()
compressao(palavra)
fim = time.time()
print('Tempo Execução Algoritmo de Compressao Tamanho Fixo:\n')
print(str(fim-inicio).replace('.',','))

probabilidade = probabilidades(palavra)
arvore = constroiArvore(probabilidade)
dicionario = constroiDicionario(arvore)
inicio = time.time()
huffman(dicionario,palavra)
fim = time.time()
print('Tempo Execução Algoritmo de Compressao Huffman:\n')
print(str(fim-inicio).replace('.',','))
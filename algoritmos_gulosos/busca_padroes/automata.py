def algoritmo_automata(palavra, texto):
    ocorrencias = []
    indice = 0
    for k, caractere in enumerate(texto):
        if palavra[indice] == caractere:
            indice += 1
            if indice == len(palavra):
                ocorrencias.append((k - len(palavra) + 1, k + 1))
                indice = 0
        elif palavra[0] == caractere:
            indice = 1
        else:
            indice = 0
    return ocorrencias

texto = "eeffgfgfgee"
palavra = 'fgfg'
ocorrencias = algoritmo_automata(palavra, texto)
print(ocorrencias)

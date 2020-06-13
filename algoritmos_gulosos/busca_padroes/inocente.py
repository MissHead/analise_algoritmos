def algoritmo_inocente(texto, palavra):
    
    for i in range(0,len(texto)-len(palavra)+1):
        j = 0
        while j < len(palavra) and palavra[j] == texto[i+j]:
            j = j + 1
        if j == len(palavra):
            return i
    return -1

texto = "analise de algoritmo"
palavra = "de"
print (algoritmo_inocente(texto, palavra))
def kmp(palavra, texto): 
	M = len(palavra) 
	N = len(texto) 
	maior_prefixo = [0]*M 
	j = 0
	lista_maior_prefixo(palavra, M, maior_prefixo) 
	i = 0 
	while i < N: 
		if palavra[j] == texto[i]: 
			i += 1
			j += 1

		if j == M: 
			print (i-j)
			j = maior_prefixo[j-1] 
		elif i < N and palavra[j] != texto[i]: 
			if j != 0: 
				j = maior_prefixo[j-1] 
			else: 
				i += 1

def lista_maior_prefixo(palavra, M, maior_prefixo): 
	len = 0
	maior_prefixo[0] 
	i = 1
	while i < M: 
		if palavra[i]== palavra[len]: 
			len += 1
			maior_prefixo[i] = len
			i += 1
		else: 
			if len != 0: 
				len = maior_prefixo[len-1] 
			else: 
				maior_prefixo[i] = 0
				i += 1

texto = "aaaccbabacabacbacbbcbbacababbbaacababcbcbcbbcbbbcbbacabababcbabcbccccbababcabb"
palavra = "acaba"
kmp(palavra, texto) 

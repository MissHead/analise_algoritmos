## IESB
**Disciplina: Análise de Algoritmos**

1º/2020

## SUBSET SUM *(Soma de subconjuntos)*
  

 ***1º parte:***

a) Implementar a solução recursiva do *subset sum* que informa se existe algum subconjunto que é igual a capacidade informada.

b) Demonstrar a complexidade de forma matemática através do método da expansão.

c) Demonstrar a complexidade do algoritmo comparando ao gráfico das complexidades padrão.

 ***2º parte:***

a) Implementar a solução do *subset sum* através de programação dinâmica que informe pelo menos 1 subconjunto que atende a capacidade informada.

b) Demonstrar a complexidade do algoritmo através da contagem de instruções.

c) Demonstrar a complexidade do algoritmo comparando ao gráfico das complexidades padrão.

 ***3º parte:***

a) Implementar a solução do *subset sum* utilizando o método de *backtracking* resultando em TODOS os subconjuntos que atendem a capacidade informada.

b) Demonstrar a complexidade do algoritmo através da contagem de instruções em caso não recursivo, ou através do método da expansão caso recursivo.

c) Demonstrar a complexidade do algoritmo através da comparação com o gráfico das complexidades padrão.

# Complexidades padrão:

 - O(1)

 - O(n)

 - O(logn)

 - O(nlogn)

 - O(n²)

 - O(n³)...

 - O(2^n)

> Data de entrega: 21/04/2020


## TABELA DINÂMICA *(dynamic table / unbounded array)*

a) calcular o tempo médio (5 execuções) de 100.000.000 de inserções e 100.000.000 de remoções em um vetor de tamanho fixo de 100.000.000.

b) calcular o tempo médio (5 execuções) de 100.000.000 de inserções e 100.000.000 de remoções em um vetor dinâmico. Com aumento * 2 e diminuição /2.

c) calcular o tempo médio (5 execuções) de 100.000.000 de inserções e 100.000.000 de remoções em um vetor dinâmico. Com aumento * 3 e diminuição /3.

d) Qual a complexidade de tempo das alternativas A,B e C.

e) Dobrar ao invés de triplicar o tamanho  na tabela dinâmica é pior ou melhor ? Em qual sentido? Justifique.

f) faça a dedução matemática da complexidade da utilização da tabela dinâmica.

> Data de entrega: 30/04/2020

## ALGORITMOS GULOSOS 

*(mochila fracionária/sequencia de tarefas/busca padroes/compressao palavras/huffman)*

1) Implemente a solução para o problema da mochila frácionária que receba do usuário uma capacidade C, um número inteiro positivo N e 2 vetores de tamanho N que correspondem ao Peso e o valor de cada um dos N elementos. É obrigatória a utilização de uma solução gulosa.

2) Encontre algum problema que pode ser resolvido com algoritmo guloso, e implemente sua solução. Demonstre a complexidade para solução do problema e gere um relatório com os tempos de execução em relação ao aumento da entrada.


> Data de entrega: 15/05/2020


1) Implemente um programa que receba uma string de tamanho N sendo N <= 1000000 e utilizando o método de código que tamanho
fixo diga qual o custo computacional para se comprimir essa string.

2) Implemente um programa que receba uma string de tamanho N sendo N <= 1000000 e utilizando o algorítmo de huffman diga qual o custo computacional para se comprimir essa string.


> Data de entrega: 29/05/2020


Fazer a leitura e interpretação da seguinte parte teórica: Link https://www.ime.usp.br/~pf/analise_de_algoritmos/aulas/string-match.html

    - Busca de uma palavra em um texto
    
    - O problema
    
    - Algoritmo inocente
    
    - Maior prefixo de P que é sufixo de T
    
    - Algoritmo do autômato
    
    - Correção do algoritmo
    
    - Consumo de tempo
    
    - Pré-processamento
    
    - Consumo de tempo total
    
1)  Implemente a Solução Inocente

2)  Resolver os exercícios:

## Parte 1

1. O algoritmo É-Sufixo produz resultado correto se n < m? 

2. Que acontece se a linha 2 de É-Sufixo for trocada por "enquanto P[l] = T[k−m+l] e l ≥ 1 faça"? 

3. Aplique o algoritmo Inocente à palavra P = 0001 e ao texto T = 000010001010001. 

3) Resolver os exercícios:

## Parte 2

1. Posso trocar a linha 2 por Busca-De-Palavra-Em-Texto por "para k crescendo de 1 até n−m+1 faça"?

2. Posso trocar a linha 2 por Busca-De-Palavra-Em-Texto "para k crescendo de m até n faça"? 

4)  Implemente a Solução de BoyerMore
    
5)  Implemente a solução KMP


## BONUS

5)  Implemente a busca de string com automatos inclusive seu pré processamento.

6)  Resolver o exercício:

## Parte 3

1. A linha q = 0 da tabela D é realmente necessária?


> Data de entrega: 13/06/2020    


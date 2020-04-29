#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define tam 100000000
#define execucoes 5
#define aumento 2

typedef struct tabeladinamica
{
    long int tamanho;
    long int qtd;
    long int * vet;
}tabeladinamica;

long int * aloca_vetor(long int qtd);
void mostra_vetor(long int * vet , long int qtd);
long int * copia(long int * vet1, long int * vet2, long int qtd);
void incluir(tabeladinamica * tab, long int x);
void remover(tabeladinamica * tab);
tabeladinamica * aloca_tabela();

int main()
{
    int i;
    tabeladinamica * tabela;
    tabela = aloca_tabela();
    tabela->vet = aloca_vetor(tam);
    tabela->tamanho = tam + 1;

    double tempo_gasto = 0.0;
    clock_t comeco = clock();

    for(i = 0; i < execucoes; i++) 
    {
	    for(i = 0; i < tam; i++) 
        {
	    	incluir(tabela, 1);
		}
		for(i = 0; i < tam; i++) 
        {
	    	remover(tabela);
		}
	}    	

    clock_t fim = clock();
    tempo_gasto += (double)(fim - comeco)/CLOCKS_PER_SEC;
    printf("\n Tempo em segundos: %f \n", tempo_gasto);

    return 0;
}

tabeladinamica * aloca_tabela()
{
    tabeladinamica * novo;
    novo = (tabeladinamica*)malloc(sizeof(tabeladinamica));
    novo->qtd = 0;
    novo->tamanho = 0;
    novo->vet = NULL;
    return novo;
}

void incluir(tabeladinamica * tab, long int x)
{
    long int * aux = NULL;
    long int i;
    if(tab->tamanho==0)
    {
        tab->vet = (long int *)malloc(sizeof(long int)* 1);
        tab->tamanho = 1;
    }
    if(tab->tamanho == tab->qtd)
    {
        long int tamanho_vetor = tab->tamanho * aumento;
        aux = aloca_vetor(tamanho_vetor);
        aux = copia(tab->vet, aux, tab->qtd);
        free(tab->vet);
        tab->vet = aux;        
        tab->tamanho = tamanho_vetor;
    }
    tab->vet[tab->qtd] = x;
    tab->qtd++;
}

void remover(tabeladinamica * tab)
{
    long int * aux = NULL;
    long int meio;
    long int i;
    if (tab->qtd == 0)
    {
        printf("\n tabela vazia");
    }
    tab->vet[tab->qtd - 1] = 0;
    tab->qtd--;
    meio = tab->tamanho / (2*aumento);
    if (tab->qtd == meio && tab->qtd != 1)
    {
        aux = aloca_vetor(meio);
		aux = copia(tab->vet, aux, tab->qtd);
        free(tab->vet);
        tab->vet = aux;
        tab->tamanho = meio;
    }
}

long int * aloca_vetor(long int qtd)
{
    int i;
    long int * novo;
    novo = (long int *)malloc(sizeof(long int )* qtd);
    for(i=0;i<qtd;i++)
    {
        novo[i] = 1;
    }
    return novo;
}

void mostra_vetor(long int * vet , long int qtd)
{
    int i;
    for(i=0;i<qtd;i++)
    {
        printf(" %ld",vet[i]);
    }
    printf("\n");
}

long int * copia(long int * vet1, long int * vet2, long int qtd) {
    int i;
    for(i=0; i<qtd; i++)
    {
        vet2[i] = vet1[i];
    }
    return vet2;
}
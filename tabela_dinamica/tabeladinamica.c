#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define tam 100000000

typedef struct tabeladinamica
{
    long int tamanho;
    long int qtd;
    long int * vet;
}tabeladinamica;

long int * aloca_vetor(long int qtd);
void mostra_vetor(long int * vet , long int qtd);
void copia(long int * vet1, long int  * vet2, long int qtd);
void incluir(tabeladinamica * tab, long int x);
void remover(tabeladinamica * tab);
tabeladinamica * aloca_tabela();

int main()
{
    int i;
    tabeladinamica * tabela;
    tabela = aloca_tabela();

    double tempo_gasto = 0.0;
    clock_t comeco = clock();
    for(i=0; i<5; i++)
    {
        incluir(tabela, i+1);
    }
    for(i=0; i<5; i++)
    {
        remover(tabela);
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
        aux = (long int *)malloc(sizeof(long int)*(2 * tab->tamanho));
        
        for(i=0; i<tab->qtd; i++)
        {
            aux[i] = tab->vet[i];
        }
        free(tab->vet);
        tab->vet = aux;
        tab->tamanho = tab->tamanho*2;
    }
    tab->vet[tab->qtd] = x;
    tab->qtd++;
}

void remover(tabeladinamica * tab)
{
    long int * aux = NULL;
    long int quarto;
    long int i;
    if (tab->qtd == 0)
    {
        printf("\n tabela vazia");
    }
    tab->vet[tab->qtd - 1] = 0;
    tab->qtd--;
    quarto = tab->tamanho / 4;
    if (tab->qtd == quarto && tab->qtd != 1)
    {
        aux = (long int *)malloc(sizeof(long int) * (tab->tamanho/2));
        for(i=0; i<tab->qtd; i++)
        {
            aux[i] = tab->vet[i];
        }
        free(tab->vet);
        tab->vet = aux;
        tab->tamanho = tab->tamanho/2;
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

void copia(long int * vet1, long int  * vet2, long int qtd)
{
    int i;
    for(i=0;i<qtd;i++)
    {
        vet2[i] = vet1[i];
    }
}
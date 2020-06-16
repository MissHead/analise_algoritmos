#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

int KaratsubaOfman(long int u, long int v, int n)
{
    if (n < 3)
        return u*v;
    else
    {
        long int m = n/2;
        long int p = u/pow(10,m);
        long int q = u*pow(10,m);
        long int r = v/pow(10,m);
        long int s = v*pow(10,m);
        long int pr = KaratsubaOfman (p, r, m);
        long int qs = KaratsubaOfman (q, s, m);
        long int y = KaratsubaOfman (p+q, r+s, m+1);
        long int x = (pr*pow(10,2*m)) + ((y-pr-qs)*pow(10,m)) + qs;
        return  x;
    }
}
int main()
{
    long int u = 9; 
    long int v = 9; 
    int n = 1;
    double tempo_gasto = 0.0;
    clock_t comeco = clock();
    KaratsubaOfman(u, v, n);
    clock_t fim = clock();
    tempo_gasto += (double)(fim - comeco)/CLOCKS_PER_SEC;
    printf("\n n = %d tempo em segundos: %f \n", n, tempo_gasto);

    u = 99; 
    v = 99; 
    n = 2;
    tempo_gasto = 0.0;
    comeco = clock();
    KaratsubaOfman(u, v, n);
    fim = clock();
    tempo_gasto += (double)(fim - comeco)/CLOCKS_PER_SEC;
    printf("\n n = %d tempo em segundos: %f \n", n, tempo_gasto);

    u = 999; 
    v = 999; 
    n = 3;
    tempo_gasto = 0.0;
    comeco = clock();
    KaratsubaOfman(u, v, n);
    fim = clock();
    tempo_gasto += (double)(fim - comeco)/CLOCKS_PER_SEC;
    printf("\n n = %d tempo em segundos: %f \n", n, tempo_gasto);

    u = 9999; 
    v = 9999; 
    n = 4;
    tempo_gasto = 0.0;
    comeco = clock();
    KaratsubaOfman(u, v, n);
    fim = clock();
    tempo_gasto += (double)(fim - comeco)/CLOCKS_PER_SEC;
    printf("\n n = %d tempo em segundos: %f \n", n, tempo_gasto);

    u = 99999; 
    v = 99999; 
    n = 5;
    tempo_gasto = 0.0;
    comeco = clock();
    KaratsubaOfman(u, v, n);
    fim = clock();
    tempo_gasto += (double)(fim - comeco)/CLOCKS_PER_SEC;
    printf("\n n = %d tempo em segundos: %f \n", n, tempo_gasto);

    u = 999999; 
    v = 999999; 
    n = 6;
    tempo_gasto = 0.0;
    comeco = clock();
    KaratsubaOfman(u, v, n);
    fim = clock();
    tempo_gasto += (double)(fim - comeco)/CLOCKS_PER_SEC;
    printf("\n n = %d tempo em segundos: %f \n", n, tempo_gasto);

    u = 9999999; 
    v = 9999999; 
    n = 7;
    tempo_gasto = 0.0;
    comeco = clock();
    KaratsubaOfman(u, v, n);
    fim = clock();
    tempo_gasto += (double)(fim - comeco)/CLOCKS_PER_SEC;
    printf("\n n = %d tempo em segundos: %f \n", n, tempo_gasto);

    u = 99999999; 
    v = 99999999; 
    n = 8;
    tempo_gasto = 0.0;
    comeco = clock();
    KaratsubaOfman(u, v, n);
    fim = clock();
    tempo_gasto += (double)(fim - comeco)/CLOCKS_PER_SEC;
    printf("\n n = %d tempo em segundos: %f \n", n, tempo_gasto);

    u = 999999999; 
    v = 999999999; 
    n = 9;
    tempo_gasto = 0.0;
    comeco = clock();
    KaratsubaOfman(u, v, n);
    fim = clock();
    tempo_gasto += (double)(fim - comeco)/CLOCKS_PER_SEC;
    printf("\n n = %d tempo em segundos: %f \n", n, tempo_gasto);

    u = 9999999999; 
    v = 9999999999; 
    n = 10;
    tempo_gasto = 0.0;
    comeco = clock();
    KaratsubaOfman(u, v, n);
    fim = clock();
    tempo_gasto += (double)(fim - comeco)/CLOCKS_PER_SEC;
    printf("\n n = %d tempo em segundos: %f \n", n, tempo_gasto);

    u = 99999999999; 
    v = 99999999999; 
    n = 11;
    tempo_gasto = 0.0;
    comeco = clock();
    KaratsubaOfman(u, v, n);
    fim = clock();
    tempo_gasto += (double)(fim - comeco)/CLOCKS_PER_SEC;
    printf("\n n = %d tempo em segundos: %f \n", n, tempo_gasto);

    u = 999999999999; 
    v = 999999999999; 
    n = 12;
    tempo_gasto = 0.0;
    comeco = clock();
    KaratsubaOfman(u, v, n);
    fim = clock();
    tempo_gasto += (double)(fim - comeco)/CLOCKS_PER_SEC;
    printf("\n n = %d tempo em segundos: %f \n", n, tempo_gasto);

    u = 9999999999999; 
    v = 9999999999999; 
    n = 13;
    tempo_gasto = 0.0;
    comeco = clock();
    KaratsubaOfman(u, v, n);
    fim = clock();
    tempo_gasto += (double)(fim - comeco)/CLOCKS_PER_SEC;
    printf("\n n = %d tempo em segundos: %f \n", n, tempo_gasto);

    u = 99999999999999; 
    v = 99999999999999; 
    n = 14;
    tempo_gasto = 0.0;
    comeco = clock();
    KaratsubaOfman(u, v, n);
    fim = clock();
    tempo_gasto += (double)(fim - comeco)/CLOCKS_PER_SEC;
    printf("\n n = %d tempo em segundos: %f \n", n, tempo_gasto);

    u = 999999999999999; 
    v = 999999999999999; 
    n = 15;
    tempo_gasto = 0.0;
    comeco = clock();
    KaratsubaOfman(u, v, n);
    fim = clock();
    tempo_gasto += (double)(fim - comeco)/CLOCKS_PER_SEC;
    printf("\n n = %d tempo em segundos: %f \n", n, tempo_gasto);

    u = 9999999999999999; 
    v = 9999999999999999; 
    n = 16;
    tempo_gasto = 0.0;
    comeco = clock();
    KaratsubaOfman(u, v, n);
    fim = clock();
    tempo_gasto += (double)(fim - comeco)/CLOCKS_PER_SEC;
    printf("\n n = %d tempo em segundos: %f \n", n, tempo_gasto);

    u = 99999999999999999; 
    v = 99999999999999999; 
    n = 17;
    tempo_gasto = 0.0;
    comeco = clock();
    KaratsubaOfman(u, v, n);
    fim = clock();
    tempo_gasto += (double)(fim - comeco)/CLOCKS_PER_SEC;
    printf("\n n = %d tempo em segundos: %f \n", n, tempo_gasto);

    u = 999999999999999999; 
    v = 999999999999999999; 
    n = 18;
    tempo_gasto = 0.0;
    comeco = clock();
    KaratsubaOfman(u, v, n);
    fim = clock();
    tempo_gasto += (double)(fim - comeco)/CLOCKS_PER_SEC;
    printf("\n n = %d tempo em segundos: %f \n", n, tempo_gasto);

    return 0;
}
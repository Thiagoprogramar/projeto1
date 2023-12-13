#include <stdio.h>;

int main ()
{

    int thiago = 0;
    int vetor1[4] = {'1','2','3','4'};
    int vetor2[100];
    int i,j;
    int soma = 0;

    for(i = 0; i < 100; i++ )
    {
        vetor2[i] = i*2+1;    
        printf("o valor da posicao %d é %d \n",i,vetor2[i]);
        soma = soma + i;
    }
    printf("o resultado da soma dos numeros é %d", soma);


return 0;
}
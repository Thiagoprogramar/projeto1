#include <stdio.h>;

int main ()
{

    int thiago = 0;
    int vetor1[4] = {'1','2','3','4'};
    int vetor2[10];
    int i,j,soma;

    for(i = 0; i < 10; i++ )
    {
        vetor2[i] = i;    
        printf("o valor da posiçao %d é %d",i,vetor2[i]);
        soma = soma + i;
    }
    printf("o resultado da soma dos numeros é %d", soma);


return 0;
}
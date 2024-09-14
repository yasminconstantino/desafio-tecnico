/*Técnica:

1) Observe o trecho de código abaixo: 

int INDICE = 13, SOMA = 0, K = 0;

Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?
o valor de soma será 91, pois mesmo que o valor atual de K seja 13, o loop irá parar, mas ainda é executado mais um vez, o que resulta em SOMA valendo 91. Segue codigo em C com o exemplo.*/

#include <stdio.h>

int main () {
	int INDICE = 13, SOMA = 0, K = 0;
	
	while (K < INDICE) {
    	K = K + 1;
    	SOMA = SOMA + K;
	    printf("%d\n", SOMA);
	}
	printf("%d", SOMA);
}

#include <stdio.h>

int main() {
    int altura = 6;
    int n = 6;
    int base = 2 * n - 1;
    
    for (int contAltura = 0; contAltura < altura; contAltura++){
        int contMax = (base / 2) - contAltura;
        int cont = 0;
        for (int contLinha = 0; contLinha < base; contLinha++){
            if (cont == contMax){
                for (int i = 0; i < base - (contMax * 2); i++){
                    printf("*");
                }
            } else {
                printf(" ");
            }
            cont++;
        }
        printf("\n");
    }
    return 0;
}
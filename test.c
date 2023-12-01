#include <stdio.h>

int main(void){
    int i,n,x = 0;
    for (i = 0; i < 10; i++){
        printf("\ndigite 1(ganhou) 2(emppatou) 3(perdeu)\n");
        scanf("%d", &n);

        if(n == 1){
            x = x + 3;
            printf("o time esta com (%d) pontos", x);
        }
        else if(n == 2){
            x = x + 1;
            printf("o time esta com (%d) pontos", x);
        }
        else if(n == 3){
            x = x + 0;
            printf("o time esta com %d pontos", x);
        }
        else{
            printf("numero invalido");
        }
    }
}

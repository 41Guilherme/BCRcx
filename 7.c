#include <stdio.h>

void verifica(int x){
    for (int i = 1; i <= x; i++)
    {
        if (i % 3 == 0 && i % 5 == 0){
            printf("Fizz Buzz\n");
        }else{
            if (i % 5 == 0){
                printf("Buzz\n");
            }else{
                if (i % 3 == 0){
                    printf("Fizz\n");
                }else{
                    printf("%d\n",i);
                }
            }
        }
    }
    
}

void main(){

    int n;
    scanf("%d",&n);

    if (n <= 100){
        verifica(n);
    }
    
}

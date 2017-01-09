#include <stdio.h>
#include <cs50.h>

int main(void){
    int n = -1;
    while (n < 0 || n > 23){
        printf("Height: ");
        n = get_int();
    }
    for (int i = 0; i < n; ++i){
        for (int j = n - 1 - i; j > 0; --j){
            printf(" ");
        }
        for (int z = i+1; z > 0; --z){
            printf("#");
        }
        printf("  ");
        for (int z = i+1; z > 0; --z){
            printf("#");
        }
        printf("\n");
    }
}
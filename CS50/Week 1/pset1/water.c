#include <stdio.h>
#include <cs50.h>

int main(void){
    printf("Minutes: ");
    int mins = get_int();
    printf("Bottles: %i\n", mins * 192 / 16);
}
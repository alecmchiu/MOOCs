#define _XOPEN_SOURCE

#include <stdio.h>
#include <string.h>
#include <cs50.h>
#include <unistd.h>

int main(int argc, string argv[]){
    if (argc != 3){
        printf("Usage: ./hasher text salt\n");
        return 1;
    }
    printf("%s\n", crypt(argv[1],argv[2]));
}
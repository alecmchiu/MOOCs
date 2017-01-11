#include <stdio.h>
#include <string.h>
#include <cs50.h>
#include <ctype.h>

int main(void){
    
    //prompt user for name
    string name = get_string();
    
    //check if first character is a letter
    if (name[0] > 64 && name[0] < 123){
        printf("%c",toupper(name[0]));
    }
    
    //iterate through the rest of the string
    for (int i = 1, n = strlen(name); i < n; ++i){
        
        //check for paradigm " *" (space and letter)
        if (name[i-1] == ' ' && name[i] < 123 && name[i] > 64){
            printf("%c",toupper(name[i]));
        }
    }
    printf("\n");
    return 0;
}
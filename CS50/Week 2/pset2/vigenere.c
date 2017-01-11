#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[]){
    
    //check for args
    if (argc != 2){
        printf("Usage: ./vigenere k\n");
        return 1;
    }
    
    string k = argv[1];
    int key_length = strlen(k);
    
    //check if key has illegal characters
    for (int i = 0; i < key_length; ++i){
        if (k[i] < 'A' || k[i] > 'z' || (k[i] > 'Z' && k[i] < 'a' )){
            printf("Usage: ./vigenere k\n");
            return 1;
        }
    }
    
    //prompt plain text
    printf("plaintext: ");
    string plaintext = get_string();
    
    printf("ciphertext: ");
    
    //keep track of key position
    int pos = 0;
    
    //iterate through plaintext
    for (int i = 0, n = strlen(plaintext); i < n; ++i){
        
        //alterations if capital
        if (plaintext[i] >= 'A' && plaintext[i] <= 'Z'){
            
            //shift ASCII code to 1-26, add shift, loop, restore ASCII code
            char new_char = (plaintext[i] - 'A' + toupper(k[pos]) - 'A') % 26 + 'A';
            printf("%c",new_char);
            
            //advance and loop key position
            pos++;
            pos %= key_length;
        }
        
        //alterations if lowercase
        else if (plaintext[i] >= 'a' && plaintext[i] <= 'z'){
            char new_char = (plaintext[i] - 'a' + toupper(k[pos]) - 'A') % 26 + 'a';
            printf("%c",new_char);
            pos++;
            pos %= key_length;
        }
        
        //do nothing if not letter
        else {
            printf("%c",plaintext[i]);
        }
    }
    
    printf("\n");
    return 0;
}
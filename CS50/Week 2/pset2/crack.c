#define _XOPEN_SOURCE

#include <stdio.h>
#include <string.h>
#include <cs50.h>
#include <unistd.h>

//check if hash is the same
bool check_hash(string password, string salt, string correct){
    if (strcmp(crypt(password,salt),correct) == 0){
        printf("%s\n",password);
        return true;
    }
    else {
        return false;
    }
}

int main(int argc, string argv[]){
    
    //check if correct arg count
    if (argc != 2){
        printf("Usage: ./crack hash\n");
        return 1;
    }
    
    string correct = argv[1];
    
    char salt[2] = {argv[1][0], argv[1][1]};
    
    //create alphabet
    char alphabet[52];
    for (int i = 0; i < 26; ++i){
        alphabet[i] = i + 'A';
    }
    for (int i = 0; i < 26; ++i){
        alphabet[i+26] = i + 'a';
    }
    
    //brute force iteration
    for (int pw_len = 1; pw_len < 5; ++pw_len){
        
        //variable length array
        char potential[pw_len];
        
        //will generate all passwords of size 1-4
        //will compare hash of all those passwords for match
        
        //check size 1
        for (int i = 0; i < 52; ++i){
            potential[0] = alphabet[i];
            if (pw_len == 1){
                if(check_hash(potential, salt, correct)){
                    return 0;
                }
            }
            
            //check size 2
            else if (pw_len >= 2){
                for (int j = 0; j < 52; ++j){
                    potential[1] = alphabet[j];
                    if (pw_len == 2){
                        if(check_hash(potential, salt, correct)){
                            return 0;
                        }
                    }
                    
                    //check size 3
                    else if (pw_len >= 3){
                        for (int k = 0; k < 52; ++k){
                            potential[2] = alphabet[k];
                            if (pw_len == 3){
                                if(check_hash(potential, salt, correct)){
                                    return 0;
                                }
                            }
                            
                            //check size 4
                            else if (pw_len == 4){
                                for (int w = 0; w < 52; ++w){
                                    potential[3] = alphabet[w];
                                    if(check_hash(potential, salt, correct)){
                                        return 0;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
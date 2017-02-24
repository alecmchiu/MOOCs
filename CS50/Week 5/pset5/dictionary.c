/**
 * Implements a dictionary's functionality.
 */

#include <stdbool.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

#include "dictionary.h"

/**
 * Trie node definition
 */
typedef struct node {
    bool is_word;
    struct node *children[27];
} node;

node *root;

/**
 * initialize node function
 */

void initialize_node(node *n){
    n->is_word = false;
    for (int i = 0; i < 27; ++i){
        n->children[i] = NULL;
    }
    return;
}

/**
 * Returns true if word is in dictionary else false.
 */
bool check(const char *word)
{
    node *current = root;
    
    int i = 0;
    char c = word[i];
    
    while (word[i] != '\0' && word[i] != '\n'){
        c = tolower(c);
        if (c == '\''){
            c = 26;
        }
        else {
            c = c - 'a';
        }
        current = current->children[(int)c];
        if (current == NULL){
            return false;
        }
        ++i;
        c = word[i];
    }
    
    if (current->is_word == true){
        return true;
    }
    else{
        return false;
    }
}

/**
 * Loads dictionary into memory. Returns true if successful else false.
 */
bool load(const char *dictionary)
{
    if (dictionary == NULL){
        return false;
    }
    else {
        FILE *dict = fopen(dictionary,"r");
        
        root = malloc(sizeof(node));
        initialize_node(root);
        
        char *word = malloc(sizeof(char)*(LENGTH+2));
        
        while (fgets(word,LENGTH+2,dict) != NULL){
            node *current = root;
            int i = 0;
            char c = tolower(word[i]);
            while (c != '\0' && c != '\n'){
                if (c == '\''){
                    c = 26;
                }
                else {
                    c = c - 'a';
                }
                if (current->children[(int)c] == NULL){
                    node *child = malloc(sizeof(node));
                    initialize_node(child);
                    current->children[(int)c] = child;
                    current = child;
                }
                else {
                    current = current->children[(int)c];
                }
                i++;
                c = tolower(word[i]);
            }
            if (c != '\0'){
                current->is_word = true;
            }
        }
        
        free(word);
        fclose(dict);
        return true;
    }
}

/**
 * recursive version to get size
 */

unsigned int recursive_size(node* current){
    
    unsigned int number = 0;
    
    if (current == NULL){
        return 0;
    }
    else {
        if(current->is_word == true){
            number++;
        }
    }
    
    for (int i = 0; i < 27; ++i){
        number += recursive_size(current->children[i]);
    }
    
    return number;
}

/**
 * Returns number of words in dictionary if loaded else 0 if not yet loaded.
 */
unsigned int size(void)
{
    if (root == NULL){
        return 0;
    }
    else {
        return recursive_size(root);
    }
    
}

/**
 * traverse tree to deallocate memory
 */ 

bool recursive_unload(node *current){
    
    bool empty = true;
    for (int i = 0; i < 27; ++i){
        if (current->children[i] != NULL){
            empty = false;
        }
    }
    if (empty == true){
        free (current);
        return true;
    }
    else {
        for (int i = 0; i < 27; ++i){
            if (current->children[i] != NULL){
                recursive_unload(current->children[i]);
            }
        }
    }
    
    free(current);
    
    return true;
}

/**
 * Unloads dictionary from memory. Returns true if successful else false.
 */
bool unload(void)
{
    if (root == NULL){
        return false;
    }
    else {
        return recursive_unload(root);
    }
    return false;
}

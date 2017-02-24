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
    bool is_word; //store word boolean
    struct node *children[27]; //store trie letter arrays
} node;

//keep track of root node
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
    
    //start with root node
    node *current = root;
    
    //traverse each letter
    int i = 0;
    char c = word[i];
    
    //advance the pointer while not at end of word
    while (word[i] != '\0' && word[i] != '\n'){
        c = tolower(c);
        if (c == '\''){
            c = 26;
        }
        else {
            c = c - 'a';
        }
        current = current->children[(int)c];
        
        //if the pointer is NULL, stop searching
        if (current == NULL){
            return false;
        }
        ++i;
        c = word[i];
    }
    
    //check final pointer
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
        
        //open file
        FILE *dict = fopen(dictionary,"r");
        
        //allocate and initialize root node
        root = malloc(sizeof(node));
        initialize_node(root);
        
        //allocate memory for the string
        char *word = malloc(sizeof(char)*(LENGTH+2));
        
        //grab characters until new line
        while (fgets(word,LENGTH+2,dict) != NULL){
            
            //keep track of current node
            node *current = root;
            
            //iterate through string
            int i = 0;
            char c = tolower(word[i]);
            while (c != '\0' && c != '\n'){
                if (c == '\''){
                    c = 26;
                }
                else {
                    c = c - 'a';
                }
                // if the next pointer doesn't exist, make it
                if (current->children[(int)c] == NULL){
                    node *child = malloc(sizeof(node));
                    initialize_node(child);
                    current->children[(int)c] = child;
                    current = child;
                }
                //else only advance the pointer
                else {
                    current = current->children[(int)c];
                }
                i++;
                c = tolower(word[i]);
            }
            // if end of word, set node's word boolean to true
            if (c != '\0'){
                current->is_word = true;
            }
        }
        
        //deallocate word string's memory and close file
        free(word);
        fclose(dict);
        return true;
    }
}

/**
 * recursive version to get size
 */

unsigned int recursive_size(node* current){
    
    //word counter
    unsigned int number = 0;
    
    //base cases
    if (current == NULL){
        return 0;
    }
    else {
        if(current->is_word == true){
            number++;
        }
    }
    
    //recursively add up the numbers from the children
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
    
    //check if no children
    
    bool empty = true;
    for (int i = 0; i < 27; ++i){
        if (current->children[i] != NULL){
            empty = false;
        }
    }
    
    //base case, if no children, dealloc memory
    if (empty == true){
        free (current);
        return true;
    }
    
    //else recursively check and deallocate children
    else {
        for (int i = 0; i < 27; ++i){
            if (current->children[i] != NULL){
                recursive_unload(current->children[i]);
            }
        }
    }
    
    //dealloc the root node
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

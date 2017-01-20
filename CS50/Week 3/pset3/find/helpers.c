/**
 * helpers.c
 *
 * Helper functions for Problem Set 3.
 */
 
#include <cs50.h>
#include <math.h>
#include "helpers.h"

/**
 * Returns true if value is in array of n values, else false.
 */
bool search(int value, int values[], int n)
{
    if (n <= 0){
        return false;
    }
    
    if (values[n/2] == value){
        return true;
    }
    else if (values[n/2] < value){
        //advance head pointer of array
        // n - n/2 != n/2 due to integer division
        return search(value, values + n/2 + 1, n - n/2 - 1);
    }
    else {
        return search(value, values, n/2);
    }
}

/**
 * Sorts array of n values.
 */
void sort(int values[], int n)
{
    int sorted[n];
    int pos = 0;
    for (int i = 0; i < 65536; ++i){
        for (int j = 0; j < n; ++j){
            if (values[j] == i){
                sorted[pos] = values[j];
                pos++;
            }
        }
    }
    for (int i = 0; i < n; ++i){
        values[i] = sorted[i];
    }
    return;
}

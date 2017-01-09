#include <stdio.h>
#include <cs50.h>

int main(void){
    printf("Number: ");
    long long number = get_long_long();
    int counter = 0;
    int sum2 = 0;
    int sum1 = 0;
    int first = -1;
    int second = -2;
    while (number != 0){
        if (counter % 2 == 0){
            sum1 += number % 10;
        }
        else {
            int temp = (2 * (number % 10));
            while (temp != 0){
                sum2 += temp % 10;
                temp /= 10;
            }
        }
        second = first;
        first = number % 10;
        number /= 10;
        counter++;
    }
    if ((sum1 + sum2) % 10 == 0){
        if (first == 4 && (counter == 16 || counter == 13) ){
            printf("VISA\n");
        }
        else if (first == 5 && (second < 6 && second > 0) && counter == 16){
            printf("MASTERCARD\n");
        }
        else if (first == 3 && (second == 4 || second == 7) && counter == 15){
            printf("AMEX\n");
        }
        else {
            printf("INVALID\n");
        }
    }
    else {
        printf("INVALID\n");
    }
}
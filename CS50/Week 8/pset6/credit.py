#!/usr/bin/env python3

if __name__ == '__main__':
    
    #get number
    number = int(input("Number: "))
    
    # counter to store length/keep track of character
    counter = 0
    
    # store the first two sums
    sum2 = 0
    sum1 = 0
    
    # storing the first and second number
    first = -1
    second = -2
    
    #perform computations depending on even or odd
    while (number != 0):
        if (counter % 2 == 0):
            sum1 += (number % 10)
        else:
            temp = (2 * (number % 10))
            while (temp != 0):
                sum2 += (temp % 10)
                temp //= 10
        second = first
        first = number % 10
        number //= 10
        counter += 1
        
    # check which card it belongs to
    if ((sum1+sum2) % 10 == 0):
        if (first == 4 and (counter == 16 or counter == 13)):
            print("VISA")
        elif (first == 5 and (second < 6 and second > 0) and counter == 16):
            print("MASTERCARD")
        elif (first == 3 and (second == 4 or second == 7) and counter == 15):
            print("AMEX")
        else:
            print("INVALID")
    else:
        print("INVALID")
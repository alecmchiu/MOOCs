#!/usr/bin/env python3

if __name__ == '__main__':
    n = -1
    
    # prompt for height until valid n
    while (n < 0 or n > 23):
        n = int(input("Height: "))
        
    for i in range(n):
        
        #print spaces
        for j in range(n-1-i):
            print(" ",end="")
        
        # print one side
        for j in range(i+1):
            print("#",end="")
        
        #print spaces
        print("  ",end="")
        
        #print other side
        for j in range(i+1):
            print("#",end="")
        print()

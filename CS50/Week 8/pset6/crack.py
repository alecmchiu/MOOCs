#!/usr/bin/env python3

import crypt
import sys
import itertools

if __name__ == '__main__':
    
    # check if correct number of command line arguments
    if (len(sys.argv) != 2):
        print("Usage: python crack.py hash",file=sys.stderr)
        exit(1)
    
    # store correct hash
    correct = sys.argv[1]
    
    # get salt
    salt = correct[:2]
    
    # generate list containing all alphabet characters
    alphabet = []
    for i in range(26):
        alphabet.append(chr(i+ord('A')))
        alphabet.append(chr(i+ord('a')))
    
    # brute force search for password
    for i in range(1,5):
        for each in itertools.product(alphabet,repeat=i):
            test = "".join(each)
            if crypt.crypt(test,salt) == correct:
                print("{}".format(test))
                exit(0)
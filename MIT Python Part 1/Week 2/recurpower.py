#!/usr/bin/env python3

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if (exp == 0):
        return 1
    elif (exp == 1):
        return base
    return base * recurPower(base,exp-1)

if __name__=='__main__':
	print(recurPower(3,4))
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20  17:42:40 2020

@author: TheAre
"""

def gcd(num1, num2):

    '''This function takes in 2 numbers as input parameter and 
    returns their greatest common divisor.

    N.B: The greatest common divisor of two integers is the largest number that
    can divide the two numbers without any remainder

    Example:
    gcd(8,12) returns 4
    '''

    divisor = min(num1, num2)  
    '''The greatest possible divisor of two numbers will be the smaller number
     of the two. This makes it a great point to start my iteration and then iterate backwards
    '''
    while divisor > 0:
        if num1 % divisor == 0 and num2 % divisor == 0:
            return divisor
            break
        else:
            divisor -= 1
    
    if divisor == 0:
        return max(num1, num2)
    elif divisor < 0:
        return 'Invalid value. Integer must be greater than zero.'

print(gcd(8, 12))

print(gcd(16, 40))

print(gcd(10,25))

print(gcd(35,315))

print(gcd(42,48))
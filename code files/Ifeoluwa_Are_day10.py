# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 15:07:26 2020

@author: TheAre
"""


def sieve_of_erastos(num):
    
    '''This takes in a limiting number as parameter and returns a list of prime numbers 
        less than the number'''
    
    numbers = []
    prime_numbers = []
    
    for i in range (2, num+1):
        prime_numbers.append(i)
        
    for i in range(2, num+1):
        if i not in numbers:
            for x in range(i*i, num+1, i):
                numbers.append(x)
            
    for i in numbers:
        if i in prime_numbers:
            prime_numbers.remove(i)
            

    return (prime_numbers)       

print(sieve_of_erastos(50)) 

print(sieve_of_erastos(20))    


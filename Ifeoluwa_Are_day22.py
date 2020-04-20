# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17  18:00:30 2020

@author: TheAre
"""

def fibonacci(num):
    '''This takes in an n value as parameter and returns the nth number in the fibonacci sequence
    
    Fibonacci sequence is a sequence in which each number is an addition of the two numbers before it
    the sequence goes like 0,1,1,2,3,5,8,13,21...

    Usage:
    fibonacci(3)
    :... 1      #the third fibonacci number is 1

    fibonacci(7)
    :... 8          # the seventh fibonacci number is 8
    '''

    count = 2
    fib_number1 = 0
    fib_number2 = 1
    fib_numbers = [fib_number1, fib_number2]

    while count < num:
        fib_number1 = fib_number1 + fib_number2
        fib_numbers.append(fib_number1)
        fib_number2 = fib_number1 + fib_number2
        fib_numbers.append(fib_number2)

        count +=2

    #print(fib_numbers)
    for i in fib_numbers:
        if num-1 == fib_numbers.index(i):
            return i
    

    
    
print(fibonacci(5))

print(fibonacci(10))

print(fibonacci(25))
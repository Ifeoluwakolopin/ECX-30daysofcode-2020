# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12  17:15:02 2020

@author: TheAre
"""

def amicable(num1:int, num2:int):

    '''This function takes in two numbers and returns a Boolean value indicating whether 
    they are amicable or not.
    
    Note: --> Amicable numbers are numbers such that the proper divisor of one is the other number
          --> None of the numbers must be equal to zero'''

    divisors_num1 = 0
    divisors_num2 = 0

    for i in range(1,num1):
        if num1%i == 0:
            divisors_num1 += i
    #print(divisors_num1)
    
    for i in range(1,num2):
        if num2%i == 0:
            divisors_num2 += i
    #print(divisors_num2)
        

    if (divisors_num1 == num2) and (divisors_num2 == num1):
        return True
    else:
        return False


print(amicable(220,284))

print(amicable(24,60))
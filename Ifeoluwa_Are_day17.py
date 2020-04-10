# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10  14:14:20 2020

@author: TheAre
"""
def abundant(num):

    '''This takes in a number and returns whether or not it is abundant'''
    divisors = 0
    for i in range(1,num):
        if num%i == 0:
            divisors += i
    if divisors > num:
        return True
    else:
        return False

def sum_abundant(number):

    '''This function takes in a number 'n' as parameter and
    returns the sum of the first n abundant numbers'''

    count = 0
    sum_of_abundant = 0

    for i in range(number*10):
        if abundant(i) == True:
            #print(i)
            count +=1
            sum_of_abundant += i
            if count == number:
                break
    return ('Sum of the first {0} abundant numbers is: {1}'.format(number, sum_of_abundant))



print(sum_abundant(5))

print(sum_abundant(2))

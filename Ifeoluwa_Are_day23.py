# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17  17:14:20 2020

@author: TheAre
"""

def find_Armstrong(start, end):

    '''This function takes in two integers indicating the start and end of an interval
    it returns the armstrong numbers within that interval.
    
    Note: An armstrong number is a number that is equal to the sum of the cubes of it's digit
    
    Example:
    find_Armstrong(152, 155)
    :...  [153] 
    ** since, 1^3 + 5^3 + 3^3 = 153, then 153 is the armstrong number in that range
    '''

    armstong_numbers = []
    for number in range(start, end+1):
        number = str(number)
        sum_of_digits = 0

        for i in number:
            sum_of_digits += (int(i) ** 3)

        if sum_of_digits == int(number):
            armstong_numbers.append(int(number))

    return armstong_numbers



print(find_Armstrong(1, 1000))
print(find_Armstrong(200,500))


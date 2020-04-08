# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 21:53:31 2020

@author: TheAre
"""

import random
def password_generator(length):
    
    '''This function takes in the length of your desired password as parameter.
     It will then generate a password of you which will include 
     alphanumeric characters of upper or lower case'''
    
    count = 0; y = ''
    parameters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    if length < 8:
        print('Your Password is too weak. Password length must be more than 7')
    else:
        while count < length:
            x = random.choice(parameters)
            y += x
            count += 1
        return (y)
    
    
print(password_generator(8))
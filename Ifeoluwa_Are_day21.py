# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17  18:22:10 2020

@author: TheAre
"""

def closest_power(base, target):

    ''' This function takes in two integers as parameter, a base and a target.
    It returns the smallest number that the base number has to be raised to that brings it closest to the target number.
    
    Example:
    closest_power(2, 5)
    :.. 2       # This returns 2 since the base raised to power 2 brings it closest to the target
    
    closest_power(3, 30)
    :.. 3       # Base raised to power 3  brings it closest to target '''

    power = 1

    while True:
        num = base ** power
        if num == target:
            break
        elif num > target:
            power -= 1
            break
        elif num < target:
            power += 1
 
    return power
            


print(closest_power(3, 2))

print(closest_power(3, 19749))

print(closest_power(5, 125))

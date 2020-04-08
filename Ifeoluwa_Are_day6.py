# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 18:07:11 2020

@author: TheAre
"""

import itertools

def power_list(list1: list):
    
    ''' Takes in a list and returns the corresponding power list of the list'''
    
    pow_list = []
    for i in range(len(list1)+1):
        for j in itertools.combinations(list1, i):
            pow_list.append(list(j))
    return pow_list


print(power_list([1,2,3]))
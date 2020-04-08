# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 11:24:25 2020

@author: TheAre
"""
import math

def faithful(n):
    
    '''This function returns the nth faithful number by taking n as parameter
    '''
    
    num = []
    answer = 0;
    while n > 0:
        x = int(math.log(n,2))
        n -= (2**x)
        num.append(x)
    for i in num:
        answer += (7**i)
    return answer

print(faithful(10))


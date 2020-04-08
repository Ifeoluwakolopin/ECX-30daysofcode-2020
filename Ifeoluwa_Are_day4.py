# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 14:07:20 2020

@author: user
"""

def is_Nigerian(x: str):
    if x[0:4] == '+234' and len(x) == 14:
        return ('The Number is Nigerian')
    elif len(x) == 11:
        if x[0:3] == '080' or '090' or '081' or '070':
            return ('The Number is Nigerian')
    else:
        return ('Not Nigerian')


x = '+2349090791001'
y = '08045678911'
z = '672567863257'

print(is_Nigerian(x))
print(is_Nigerian(y))
print(is_Nigerian(z))
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20  09:34:53 2020

@author: TheAre
"""

def desc_triangle(len1, len2, len3):

    '''This function takes in the length of the 3 sides of a triangle, and returns a tuple
    containing the type of triangle and it's area.

    Example:
    desc_triangle(3,5,4) returns ('Right-Angled Triangle',6.0) '''

    triangle_types = ['Equilateral Triangle', 'Isosceles Triangle', 'Right-Angled Triangle', 'Scalene Triangle']

    #To get the area of a triangle given the three sides: Heron's Formula
    s = (len1+len2+len3) / 2
    area = (s*(s-len1)*(s-len2)*(s-len3)) ** 0.5
    
    #This little try block was so i could catch imaginary triangles with complex area.
    try:
        area = round(area, 3)
    except TypeError:
        return ('This triangle is imaginary because it has a complex area')
    
    #Type checks
    if len1==len2==len3:
        return ((triangle_types[0], area))

    elif len1==len2 or len1==len3 or len2==len3:
        return ((triangle_types[1], area))

    elif len1 != len2 and len2 != len3:
        if ((len1**2)+(len2**2)-(len3**2) == 0) or ((len1**2)-(len2**2)+(len3**2) == 0) or ((len2**2)+(len3**2)-(len1**2) == 0):
            return((triangle_types[2], area))
        else:
            return((triangle_types[3], area))



print(desc_triangle(3,5,4))

print(desc_triangle(4,8,9))

print(desc_triangle(4,4,4))

print(desc_triangle(5,8,8))

print(desc_triangle(1,2,4))
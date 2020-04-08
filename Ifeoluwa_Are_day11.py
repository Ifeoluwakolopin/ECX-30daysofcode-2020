# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 23:09:42 2020

@author: TheAre
"""
def compressor(string_num):
    
    ''' This function takes in a string of numbers as its parameter and returns
    a tuple of tuples containing a number in the string and the number of occurences
    in the original string given'''
    
    list_num = []
    final = []
    
    for i in string_num:
        list_num.append(int(i))
    list_num.sort()
    
    for i in list_num:
        count = list_num.count(i)
        final.append((i, count))
        for x in range(count-1):
            list_num.remove(i)
    
    return tuple(final) 
    
    

print(compressor('53231247234932324687548386875'))

print(compressor('13701301301'))

print(compressor('184634632447164723'))

print(compressor('36363677'))

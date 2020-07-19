# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 13:35:50 2020

@author: TheAre
"""



def bin_search(list1 : list,num: int):
    if num == (list1[-1]):
        return True
    else:
        if num in (list1[:len(list1)//2]):
            list1 = list1[:(len(list1)//2)]
            return bin_search(list1, num)
        elif num in (list1[len(list1)//2:]):
            list1 = list1[len(list1)//2:]
            return bin_search(list1, num)
        else:
            return False
       


list2 = [1,2,4,5,3,6,7,8,9,10,11]
num = 12
print(bin_search(list2, num))
         
      
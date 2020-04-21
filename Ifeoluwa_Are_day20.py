# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20  15:10:22 2020

@author: TheAre
"""

def to_mandarin(num):

     '''This function takes in an integer <=99 as its parameter and 
     returns the mandarin version as a string.'''

     mandarin = {'Yi': 1, 'Er':2, 'San':3, 'Si':4, 'Wu':5,
     'Liu':6, 'Qi':7, 'Ba': 8, 'Jiu': 9, 'Shi':10}

     keys = list(mandarin.keys())
     #print(keys)
     
     final_string = ''

     if num > 99 or num < 1:
         return('Invalid number! Please enter a number from 1-99')
     else:
          if num <= 10:
               final_string = keys[num-1]
               return final_string
          else:
               last = 0
               while num%10 != 0:
                    last += 1
                    num -=1

               first = num/10
               # So i have the format 43 = 4 * 10 + 3 (first * 10 + last)

               if first > 1 and last > 0:
                    final_string = keys[int(first)-1] + keys[9] + keys[int(last)-1]
                    return final_string
               elif last == 0:
                    final_string = keys[int(first)-1] + keys[9]
                    return final_string
               elif first == 1:
                    final_string = keys[9] + keys[int(last)-1]
                    return final_string

print(to_mandarin(15))

print(to_mandarin(87))

print(to_mandarin(70))

print(to_mandarin(101))

print(to_mandarin(4))

print(to_mandarin(99))

print(to_mandarin(24))
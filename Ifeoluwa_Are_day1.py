# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 22:14:33 2020

@author: TheAre
"""

import random

x = random.randrange(0, 100)

print('I\'ve just thought of a number between 0 and 100!')
print('Try to guess this number!')


def RandomNumber(num):
    
    '''This is a function that generates a random number that user has to guess
        It takes in the number of guesses allowed as parameter'''
    
    while num > 0:
        user_input = int(input('Guess the number: '))
        if num == 1 and user_input!= x:
            print('Sorry, no more guesses left')
            return('The correct number was ' + str(x))
            break
        if user_input == x:
            return('You guessed right!')
            break
        elif user_input > x:
            print('You guessed too high!')
            print('You have ', num-1, ' guesses left!')
            return RandomNumber(num-1)
        elif user_input < x:
            print('You guessed too Low!')
            print('You have ', num-1, ' guesses left!')
            return RandomNumber(num-1)
    

        


print(RandomNumber(5))

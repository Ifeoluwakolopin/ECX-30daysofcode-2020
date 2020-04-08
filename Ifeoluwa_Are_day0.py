# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 20:27:07 2020

@author: TheAre
"""

Scrabble_words = {1:['a','e','i','o','l','n','r','s','t','u'], 
                  2:['d','g'], 
                  3:['b','c','m','p'], 
                  4:['f','h','v','w','y'], 
                  5:['k'], 
                  8:['j','x'], 
                  10:['q','z']}

def word_score(x):
    
    '''This function takes in a string of alphabeths as input 
        and returns the Scrabble score as an integer '''
        
    score = 0
    for i in x.lower():
        for key, value in Scrabble_words.items():
            if i in value:
                score += key
    return(score)

print(word_score('quixotic')) # >>> 26
print(word_score('maximize')) # >>> 28
print(word_score('jezebel'))  # >>> 25
print(word_score('quizzify')) # >>> 41
print(word_score('fortune'))  # >>> 10
    
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 16:52:59 2020

@author: TheAre
"""

def wrapper(paragraph, char_limit):
    
    '''This taks in a paragraph and the maximum number of characters per line 
    as parameters and returns the wrapped text
    Note: The paragraph should be put in as a string and may contain escape sequence'''
    
    
    sentence = paragraph.split('\n')
    
    final = ''
    letters = []
    count = 0

    for line in sentence:

        #This is to read each character in the rawstring and add to a list.
        for i in repr(line):
            letters.append(i)

        #the repr also reads the quotation marks of the strings which we do not need in our list
        letters.remove(letters[0])
        letters.remove(letters[-1])
        
        #This counts to see if the character limit has been reached and inserts a new line when that is True
        for i in letters:
            count += 1
            final = final + i
            if count % char_limit == 0:
                final = final + '\n'
        
        letters = []
        final = final +'\n'

    return final

#This works regardless of whether or not the paragraph contains an escape sequence

print(wrapper('The boy is a very bad boy.\nHe is not smart at all.\nHe is also quite rough an ddisorderly', 5))

print(wrapper('What is a noun. A noun is a name of any person, animal, place or thing. Examples of a noun can be Aba, Bola, Tola, Chair, Dubai, Engineering', 6))

print(wrapper('Engineering Career Expo (ECX) challenge day 13 finally done!. This took a lot of thinking and redoing over and over till i got what i wanted', 8))

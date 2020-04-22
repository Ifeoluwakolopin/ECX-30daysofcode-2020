# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22  17:50:30 2020

@author: TheAre
"""

def keys_pressed(text_message):

    ''' This function takes in a text message as the input parameter and 
    returns the key presses that must be made to give the required text on a basic cell phone.

    On some basic cell phones, text messages can be sent using the numeric keypad. Each key has multiple letters associated with it, multiple key presses are needed for most letters.
    Pressing the number once generates the first letter on the key. Pressing the number 2, 3, 4 or 5 times generates the second, third, fourth or fifth character listed for that key.

    Key Symbol
    1 = (. , ? ! :)   2 = (A B C)   3 = (D E F)   4 = (G H I)   5  = (J K L)   6 = (M N O)
    7 = (P Q R S)     8 = (T U V)   9 = (W X Y Z)     0 = (space)
    
    Example:
     keys_pressed('Hello, World!') should return 4433555555666110966677755531111

    '''

    key_mapping = { 1: ['.', ',', '?', '!', ':'], 
    2: ['A', 'B', 'C'], 
    3: ['D', 'E', 'F'], 
    4: ['G', 'H', 'I'], 
    5: ['J', 'K', 'L'], 
    6: ['M', 'N', 'O'], 
    7: ['P', 'Q', 'R', 'S'], 
    8: ['T', 'U', 'V'], 
    9: ['W', 'X', 'Y', 'Z'], 
    0: [' ']}

    text_list = [i for i in text_message]

    
    #MAIN CODE
    total_key_presses =  ''

    for letter in text_list:
        for key, value in key_mapping.items():
            if letter.upper() in value:
                
                index = value.index(letter.upper())
                key_press = str(key) * (index+1)

                total_key_presses += key_press

    #This little piece checks if the message_string has some invalid characters and 
    # notifies the user that the messsage contains some characters that will not be displayed following the key_presses output
    
    allowed_charaters = []
    for i in key_mapping.values():
        for x in i:
            allowed_charaters.append(x)
    
    invalids = ''
    for i in text_list:
        if i.upper() not in allowed_charaters:
            invalids += i
            invalids += ' '
    
    if len(invalids) != 0:
        print('\n' + text_message + '\nYour message contains invalid character(s): "{0}"'.format(invalids))
    else:
        print('\n' + text_message)



    return total_key_presses


print(keys_pressed('Hello, World!'))

print(keys_pressed('This is a new day. Day 29 of the ecx 30daysofcode'))

print(keys_pressed('isolation is boringg ;-('))
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12  21:04:05 2020

@author: TheAre
"""

def find_edit_dist(string1, string2):
    
    ''' This takes in two strings and returns the edit distance between the two strings.
    the edit distance is the amount of actions it will take to make one string into the other'''

    edit_dist = 0
    one = len(string1);     two = len(string2)

    if string1 == string2:
        return edit_dist
    elif one == 0:
        return two
    elif two == 0:
        return one
    else:
        
        if one == two:

            #This asumes that if the two strings have the same length
            # editor will replace the letters that are out of place in one of the strings
            for index, i in enumerate(string1):
                if i != string2[index]:
                    edit_dist += 1
            return edit_dist
        
        else:

            if one > two:
                x = [i for i in string2] ;   y = [i for i in string1]
            else:
                x = [i for i in string1] ;   y = [i for i in string2]
            
            count = 0

            ''' The logic behind this last part. If the two strings are not the same length,
            then the editor replaces all the wrong letters in the longer string with the 
            corresponding letter in the shorter string.FIRSTLY. Then removes extra letters'''

            for i in y:
               if i in x:
                   count += 1
            edit_dist = len(y) - count
            y = [i for i in y if i in x]
            added_letters = len(x) - len(y)

            return edit_dist
               


# Basically, this function takes replacing wrong letters as it's first line of editing, 
# then removing extra letters if any...

print(find_edit_dist('gloat', 'float'))

print(find_edit_dist('camel', 'donkeys'))

print(find_edit_dist('allow', 'below'))

print(find_edit_dist('bloat', 'belss'))

print(find_edit_dist('goat', 'floater'))


                
            
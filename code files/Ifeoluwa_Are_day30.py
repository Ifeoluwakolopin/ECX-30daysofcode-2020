# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25  11:21:30 2020

@author: TheAre
"""

def nester(string_of_num):

    '''This function takes in a string of numbers and inserts a minimum number of opening 
    and closing parentheses into it such that the resulting string is balanced and each digit d is inside exactly d pairs of matching parentheses.

    Example:
    print(nester('302'))        #Output: (((3)))0((2))
    '''
    num = []

    try:
        for i in string_of_num:
            num.append(int(i))

        brackets = 0

        final_string = ''

        if int(string_of_num) == 0:
            return string_of_num


        for i in num:
            if brackets == 0:
                brackets = i
                final_string += '('* brackets
                final_string += str(i)
            else:
                if i == 0:
                    final_string += str(i)
                    brackets = i
                else:
                    if i > brackets:
                        brackets = i-brackets
                        final_string += '('* brackets
                        final_string += str(i)
                        brackets = i
                    else:
                        final_string += str(i)
                        brackets = i

        #print(final_string)  #This first part was for the opening brackets

        brackets = 0
        new_final = ')'

        for i in final_string[-1:0:-1]:
            if i == '(':
                new_final += i
            elif brackets == 0:
                brackets = int(i)
                new_final += ')'* brackets
                new_final += i
            else:
                if int(i) == 0:
                    new_final += i
                    brackets = int(i)
                else:
                    if int(i) > brackets:
                        brackets = int(i)-brackets
                        new_final += ')'* brackets
                        new_final += i
                        brackets = int(i)
                    else:
                        new_final += str(i)
                        brackets = int(i)

        if string_of_num[0] == '0':
            new_final += '0'
        else:
            new_final +='('

        #print('\n')
        return new_final[-1:0:-1]

    except ValueError:

        print('Invalid String format: String should only contain integers')



print(nester('302'))

print(nester('0000'))

print(nester('132'))

print(nester('413213'))

print(nester('42150000'))

print(nester('0312'))

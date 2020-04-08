# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 16:31:50 2020

@author: TheAre
"""



def decryptor(strng, num):
    
    '''This functions takes in your secret code and the number as parameter
    and returns the deciphered string'''
    
    alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    new_string = ''
    case_check = 0
    for i in strng:
        if i.isupper():
            case_check = 1
        else:
            case_check = 0
        if i in alphabets:
            ind = alphabets.index(i)
            if case_check == 1:
                new_string = new_string + alphabets[ind + num].upper()
            else:
                new_string = new_string + alphabets[ind + num].lower()
        else:
            new_string = new_string + i

    return new_string

#HAPPY DECIPHERING!
    
print(decryptor('Nby vis cm aiix.', 6))
print(decryptor('Rovvy pbyw dro ydrob csno...', -10))
print(decryptor("Ukq'ra kjhu fqop xacqj.", 4))
print(decryptor("Sdwp zkaoj'p gehh ukq, iwgao ukq opnwjcan", -22))
print(decryptor('Rcb mjh 9 xo cqn 30 mjhb xo lxmn lqjuunwpn!!', 17))
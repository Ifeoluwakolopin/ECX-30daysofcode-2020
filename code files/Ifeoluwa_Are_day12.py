# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 09:43:37 2020

@author: TheAre
"""

def Validate_email(email_str):
    
    '''This function takes in your email address as a string and returns if the
    email is valid or invalid
    
    Expected string format: someone@example.top_Domain '''
    
    someone = 'abcdefghijklmnopqrstuvwxyz0123456789.!#$%^&*()_-=+\\|/'
    example = 'abcdefghijklmnopqrstuvwxyz0123456789-'
    top_domain = 'abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXYZ.'
    mail = []
    
    ini = email_str.split('@')
    mail.append(ini[0])
    
    print('-----------------------------------------------')
    print(email_str)
    
    #This for loop is to split the given string into the various parts
    for i in ini[1].split('.'):
        mail.append(i)
    #print (mail)
    
    #This checks the part of the string before the '@' sign
    for i in mail[0]:
        if i not in someone:
            return 'The email address is invalid'
        elif mail[0].count('.') > 1:
            return 'The email address is invalid'
        else:
            x = True
    
    #This checks the 'example' part       
    for i in mail[1]:
        if i not in example:
            return 'The email address is invalid'
        else:
            y = True
    
    '''this is incase the domain name has more than one '.' in it.
    Since i split the latter part of the string using '.' i will have to check each part separately
    to see if they obey the conditions for the top_domain part '''
    
    if len(mail) > 3:
        for q in mail[2:-1]:
            for i in q:
                if i not in top_domain:
                    return 'The email address is invalid'
                else:
                    z = True

    for i in mail[-1]:
         if i not in top_domain:
             return 'The email address is invalid'
         elif (len(mail[-1]) > 3):       #
             return 'The email address is invalid' 
         else:
             z = True 
    
    if x == y == z:
        return 'The email address is valid'
    else:
        return 'The email address is invalid'
    
    
    
''' Code is Quite Long. 
This same thing can be done in a few lines by importing Regex 
but instructions said no in_built modules.

'''  
    
    
print(Validate_email('areifeoluwa10@gmail.com')) #valid

print(Validate_email('acb.q3b@aDeat.it'))   #invalid. --->No capital letters should be in 'example'

print(Validate_email('a..gjhvj@gmail.com')) #invalid ---->'someone' should not have more than one dot

print(Validate_email('&feresa@a1club.me')) #valid

print(Validate_email('areifeoluwa@gmail.at.meaa.got.it')) #valid

print(Validate_email('acb.q3b@aeat.itjcajg')) #invalid ------> 'Not more than 3 characters after the last fullstop

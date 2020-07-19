# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21  16:48:20 2020

@author: TheAre
"""

months = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 
'may': 5, 'june': 6, 'july': 7, 'august': 8, 'september': 9, 'october': 10, 
'november': 11, 'december': 12}

def magic_date(date):

    '''This function takes in a date written in the form "month day,year" 
    example: "June 10,1960" as input parameter and returns a Boolean indicating if that the date is magic or not.
    Note: A magic date is a date where the day multiplied by the month is equal to the two-digit year. 
    For example, June 10,1960 is a magic date because June is the sixth month, and 6 times 10 is 60'''

    # This helps me get the date into a useable form
    date_list = [i for i in date]
    date_list = [' ' if  i == ',' else i for i in date_list]
    date = ''.join(date_list).split()

    # This gets what month it is by checking through the dictionary i created initially
    if date[0].lower() in months:
        x = months[date[0].lower()]
    else:
        return "Invalid Month of the Year"
    
    y = int(date[1]) ;      z = int(date[2][-2:])        #print(x, y, z)
    if x * y == z:
        return True
    else:
        return False


days_in_months = {'january': 31, 'february': 28, 'march': 31, 'april': 30, 
'may': 31, 'june': 30, 'july': 31, 'august': 31, 'september': 30, 
'october': 31, 'november': 30, 'december': 31}

names_of_months = ['january', 'february', 'march', 'april', 'may', 'june', 'july',
 'august', 'september', 'october', 'november', 'december']

def count_magic(year):

    ''' This takes in a year as input and returns a list of all the magic dates in that year'''
    
    magic_dates_in_year = []
    for i in names_of_months:
        days = days_in_months[i]

        for x in range(1, days+1):
            date = '{0} {1},{2}'.format(i.capitalize(), x, year)

            if magic_date(date) == True:
                magic_dates_in_year.append(date)

    print('\n')

    return magic_dates_in_year


print(count_magic(1960))

print(count_magic(2056))

print(count_magic(1801))

print(count_magic(234650))


#This code does not assume a leap year
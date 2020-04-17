# -*- coding: utf-8 -*-
"""
Created on Thu Apr 9  16:26:40 2020

@author: TheAre
"""
def binary_adder(num1, num2):

    '''This function takes in two binary numbers and returns the sum of the two numbers
    in binary
    '''

    if type(num1) and type(num2) == str:

        max_len = max(len(num1), len(num2))

        num1 = num1.zfill(max_len)
        num2 = num2.zfill(max_len)

        result = ''
        carry = 0

        for i in range(max_len-1, -1, -1):
            r = carry
            r += 1 if num1[i] == '1' else 0
            r += 1 if num2[i] == '1' else 0
            result = ('1' if r % 2 == 1 else '0') + result
            carry = 0 if r < 2 else 1       

        if carry !=0 : result = '1' + result

        return result.zfill(max_len)

    elif type(num1) and type(num2) == int:
        num1 = str(num1)
        num2 = str(num2)
        sum = int(num1, 2) + int(num2, 2)
        sum = bin(sum)
        sum = str(sum)
        sum = sum[2:]
        sum = int(sum)
        return sum


print(binary_adder('11', '1'))
print(binary_adder('100', '10'))
print(binary_adder('111', '111'))

print(binary_adder(100, 1101))
print(binary_adder(1,1))

'''The elif part wasn't really necessary I just put it there as another method of solving
    the question; since it doesn't count as importing a module.
    Cheers!'''
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 8  13:20:30 2020

@author: TheAre
"""



def anagram_finder(list1):
    
    anagram = []
    total = []

    ''' This function takes in a list of words as parameter and returns a list of sub-lists
    where each sub list contains all the anagrams in the original list'''

    for word  in list1:
        for other_word in list1:
            #for each word in the list, if there's another word with the same letters in it, then they are anagrams
            if word != other_word and sorted(word)==sorted(other_word):
                anagram.append(word)
                anagram.append(other_word) #add the two words to the list of anagrams
                list1.remove(other_word)    #remove the other_word


        #the for loop above may cause the initial 'word' to be repeated in the list.   
        for i in anagram:
            if anagram.count(i) > 1:
                anagram.remove(i)
        if len(anagram) > 1:
            total.append(anagram)
        anagram = []
            
                
            
    return total          

            
                


                
    



list1 = ['care','dove','vote','race','devious', 'scan','cans', 'erac', 'toy','oyt','seen','yot']
list2 = ['evade', 'toyota', 'coding', 'decoder', 'codered', 'amalgamate', 'life', 'file']
print(anagram_finder(list1))

print(anagram_finder(list2))

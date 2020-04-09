# -*- coding: utf-8 -*-
"""
Created on Wed Apr 8  17:13:20 2020

@author: TheAre
"""
'''This Program is written to take in a text file containing song lyrics
    and invert all the lines and also invert words on each line;
    to give a disordered string'''

#This is to open the .txt file of some random song lyrics i got off the web
song = open('song.txt', 'r')
song = song.read()
song = str(song)
lines = song.split('\n')
#print(lines)

final = open('disordered.txt', 'w')

#This for loop will first invert the whole text. i.e The firstline becomes the last and vice-versa
for line in lines:
    x = lines.index(line)
    x += 1
    words = lines[-x].split()
    string = ''


    #For each line, the first word becomes the last and vice-versa
    for i in words:
        y = words.index(i)
        y+=1        
        string = string + words[-y] + ' '
    final.write(string + '\n')
    
final.close()


# x and y were used to store the index so i could call them from behind.
# I have included both the song.txt file and the disordered.txt in my submission


# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 14:23:07 2020

@author: TheAre
"""

def captains_room(room_list):
    
    '''This function takes in a list as parameter and returns the captain's room'''

    new_list = []
    while room_list:
        minimum = room_list[0]
        for i in room_list:
            if i < minimum:
                minimum = i
        new_list.append(minimum)
        room_list.remove(minimum)
    
    final_room = []
    wrong_room = []  

    for i in range(len(new_list)):
        
        if len(new_list) == 1:  #IF ONLY ONE ROOM IS GIVEN, IT WOULD BE THE CAPTAIN'S
            final_room = new_list
            return final_room
            break
           
        if new_list[0] == new_list[1]:
            wrong_room.append(new_list[0])
            new_list.remove(new_list[0])
            new_list.remove(new_list[0])


        try:
            if new_list[0] != new_list[1]:
                if new_list[0] in wrong_room:
                    new_list.remove(new_list[0])

                else:
                    final_room.append(new_list[0])
                    new_list.remove(new_list[0]) 
                    return final_room
                    break
        except IndexError:
            return new_list


room_list = [1,2,3,1,4,2,3,3,4,4,4,5,7,5,6,7,8,6,9,4,4,5,7,9,9,6,7,6,9,5,4,3,]

print(captains_room(room_list))

room_list1 = [2,1,1,5,8,6,9,6,7,8,9,4,5,2,2,4,3,4,6,5,4,4,5,5,6,9,10,23,1,2,1,2,12,23,10,12]

print(captains_room(room_list1))


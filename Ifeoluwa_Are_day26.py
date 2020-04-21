# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20  11:10:30 2020

@author: TheAre
"""

def gpa_calculator(scores_list, units_list):

    ''' This function takes in 2 lists as parameters 
    (The list of scores in courses and the list of their corresponding units) and returns the GPA.
     The University of Lagos grading system is used and is as follows:

    Score       Grade   Points
    70 and above    A       5
    60 to 69        B       4
    50 to 59        C       3
    45 to 49        D       2    
    40 to 44        E       1
    39 and below    F       0
    
    Example:
    gpa_calculator([71,72,73,74,75],[3,2,2,1,2]) returns 5.0

    '''
    
    #Incidentally, the index of the values in this list corresponds to the relative points.
    grading_system = [range(0,39), range(40,45), range(45, 50), 
    range(50,60), range(60,70), range(70, 101)]

    total_units = sum(units_list)
    total_course_points = 0

    for i in scores_list:
        ind = scores_list.index(i)

        for x in grading_system:
            if i in x:
                point = grading_system.index(x)
                #print(point)
        
        if i < 0 or i>100:
            point = 0
        course_points = point * units_list[ind]

        total_course_points += course_points

    gpa = total_course_points/total_units
    gpa = round(gpa, 2)

    return (gpa)

                


print(gpa_calculator([71,72,73,74,75],[3,2,2,1,2]))

print(gpa_calculator([45,52,76, 87,56],[3,2,2,1,2]))

print(gpa_calculator([71,92,73,74,55,67],[3,3,2,2,2,2]))

print(gpa_calculator([78,72,59,67,56,67,66,45,43], [1,3,2,3,3,2,1,2,1]))
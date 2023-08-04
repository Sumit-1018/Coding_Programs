# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 20:56:46 2022

@author: Parnika
"""

# Python program to demonstrate
# Addition of elements in a Set
 
# Creating a Set
set1 = set()
print("Blank Set: ")
print(set1)
 
#input set
set1 = {1, 2, 3, 4, 5}
# a list of numbers to add
list_to_add = [6, 7, 8]
# add all elements of list to the set using update function
set1.update(list_to_add)
print('Updated set after adding elements using update function: ', set1)

#Add all elements from multiple lists to the set
# input set
set1 = {11, 12, 13, 14}

# 3 lists of numbers
list1 = [15, 16, 17]
list2 = [18, 19]
list3 = [30, 31, 19, 17]

# Add multiple lists
set1.update(list1, list2, list3)

#updated list
print('Updated Set after adding multiple lists using update functions: ', set1)

# Adding element and tuple to the Set using add function
set1.add(8)
set1.add(9)
set1.add((6, 7))
print("\nSet after Addition of Three elements using add function: ")
print(set1)
 

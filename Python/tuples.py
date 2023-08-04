# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 19:37:19 2022

@author: Parnika
"""
# Creating an empty tuple using tuple() function
tuple1 = tuple() 
print(tuple1) # Printing tuple1

 # mytuple = 1, 2, 3, "Data types" will also work.
mytuple = (1, 2, 3, "Data types")
print(mytuple)
print(type(mytuple))

# creating tuple with different type of values
tuple2 = (1, 2, 3, "data types") 
print(tuple2) # print created tuple
(1, 2, 3, 'data types')

# Will print integer 1 instead of a tuple.
mytuple = (1)
print(mytuple) 
print(type(mytuple)) 

#The trailing comma is mandatory for the one-element tuples.
mytuple = (1,)
print(mytuple) # Will print tuple (1,) 
print(type(mytuple)) 

#The trailing comma is completely optional for the multiple-element tuples.
mytuple = (1, 2, 3)
print(mytuple)
print(type(mytuple))

#The trailing comma is completely optional for the multiple-element tuples.
mytuple = (1, 2, 3,)
print(mytuple)
print(type(mytuple))
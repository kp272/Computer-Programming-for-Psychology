#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 09:05:33 2022

@author: kasti
"""

# import random
# import numpy as np 


### Conditional exercises
# Question 1) 
response = 1
if response == 1 or response == 2:
    print("OK")
elif response == "NaN":
    print("subject did not respond") 
else:
    print("subject pressed the wrong key")
    
# Question 2)
if response == 1 or response == 2:
    if response == 1:
        print("Correct!")
    if response == 2:
        print("Incorrect!")
elif response == "NaN":
    print("subject did not respond") 
else:
    print("subject pressed the wrong key")
    
# Question 3)
# responses 1 , 2, 'NaN' and ' ' were tested. The outputs were Correct!, Incorrect!, subject did not respond and subject pressed the wrong key.  

### For loop exercises
# Question 1)
myName = 'Kasti'
for letter in myName:
    print(letter)
    
# Question 2)
myName = 'Kasti'
counter = -1
for letter in myName:
    counter = counter + 1
    print(letter)
    print(counter)
    
# Question 3)
names = ["Amy", "Rory", "River"]
for name in names:
    print(name)
    for letter in name:
        print(letter)
        
# Question 4)
names = ["Amy", "Rory", "River"]
for name in names:
    print(name)
    letterCounter = -1
    for letter in name:
        letterCounter = letterCounter + 1
        print(letter)
        print(letterCounter)

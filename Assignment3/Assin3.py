#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 17:55:55 2022

@author: kasti
"""

# The outputs are copied under each command like so:
        # outputs


import numpy as np

### Variable operations exercises
# Question 1)
sub_code = "sub"
subnr_int = 2
subnr_str = "2"
#print(sub_code + subnr_int) --> didn't work
print(sub_code + subnr_str)
        #sub2

# Question 2)
print(sub_code + " " + subnr_str)
print(sub_code + " " + subnr_str*3) 
print((sub_code + subnr_str)*3)
print((sub_code*3)+(subnr_str*3))
        # sub 2
        # sub 222
        # sub2sub2sub2
        # subsubsub222


# =====================================================================
# =====================================================================


### List operation exercises
# Question 1)
numlist = [1,2,3]
numlist * 2
        #[1, 2, 3, 1, 2, 3]
        
# Question 2)
numarr = np.array([1,2,3])
numarr*2
        # array([2, 4, 6])

# Question 3)
strlist = ['do','re','mi','fa']
print([strlist[0]*2, strlist[1]*2, strlist[2]*2, strlist[3]*2])
        # ['dodo', 'rere', 'mimi', 'fafa']
print(strlist * 2)
        # ['do', 're', 'mi', 'fa', 'do', 're', 'mi', 'fa']
print([strlist[0], strlist[0], strlist[1], strlist[1], strlist[2], strlist[2], strlist[3], strlist[3]])
        # ['do', 'do', 're', 're', 'mi', 'mi', 'fa', 'fa']
print([[strlist[0], strlist[0]], [strlist[1], strlist[1]], [strlist[2], strlist[2]], [strlist[3], strlist[3]]])
        # [['do', 'do'], ['re', 're'], ['mi', 'mi'], ['fa', 'fa']]


# =====================================================================
# =====================================================================


### Zipping exercises
# Question 1)
first_item = []
second_item = []
images_faces_f = ["face1.png"] * 5 + ["face2.png"] * 5 + ["face3.png"] * 5 + ["face4.png"] * 5 + ["face5.png"] * 5
images_houses_f = ["house1.png"] * 5 + ["house2.png"] * 5 + ["house3.png"] * 5 + ["house4.png"] * 5 + ["house5.png"] * 5
first_item.extend(images_faces_f)
first_item.extend(images_houses_f)
first_item.extend(images_faces_f)
first_item.extend(images_houses_f)
images_faces_s = ["face1.png", "face2.png", "face3.png", "face4.png", "face5.png"] * 5
images_houses_s = ["house1.png", "house2.png", "house3.png", "house4.png", "house5.png"] * 5
second_item.extend(images_houses_s)
second_item.extend(images_faces_s)
second_item.extend(images_houses_s)
second_item.extend(images_faces_s)
cues = ['cue1'] * 50 + ['cue2'] * 50
catimgs = list(zip(first_item, second_item, cues))
np.random.shuffle(catimgs)
print(catimgs)
                # [('house2.png', 'face5.png', 'cue1'), ('house1.png', 'face3.png', 'cue2'), ('house1.png', 'face3.png', 'cue1'), ('house1.png', 'face1.png', 'cue2'), ('face1.png', 'house1.png', 'cue2'), ('face5.png', 'house4.png', 'cue2'), ('face2.png', 'house3.png', 'cue2'), ('face4.png', 'house4.png', 'cue2'), ('house5.png', 'face1.png', 'cue2'), ('house4.png', 'face4.png', 'cue2'), ('face5.png', 'house3.png', 'cue2'), ('house2.png', 'face4.png', 'cue2'), ('face2.png', 'house5.png', 'cue1'), ('house3.png', 'face4.png', 'cue2'), ('house2.png', 'face1.png', 'cue1'), ('house5.png', 'face3.png', 'cue2'), ('house2.png', 'face1.png', 'cue2'), ('face5.png', 'house4.png', 'cue1'), ('face3.png', 'house1.png', 'cue1'), ('face1.png', 'house2.png', 'cue1'), ('house5.png', 'face1.png', 'cue1'), ('house2.png', 'face2.png', 'cue2'), ('face3.png', 'house4.png', 'cue1'), ('house5.png', 'face5.png', 'cue1'), ('face3.png', 'house1.png', 'cue2'), ('house5.png', 'face2.png', 'cue1'), ('face5.png', 'house5.png', 'cue2'), ('face5.png', 'house2.png', 'cue1'), ('house4.png', 'face1.png', 'cue1'), ('face1.png', 'house3.png', 'cue1'), ('face2.png', 'house5.png', 'cue2'), ('face1.png', 'house1.png', 'cue1'), ('face2.png', 'house4.png', 'cue2'), ('house3.png', 'face4.png', 'cue1'), ('house2.png', 'face5.png', 'cue2'), ('house3.png', 'face2.png', 'cue1'), ('house3.png', 'face3.png', 'cue2'), ('face2.png', 'house1.png', 'cue2'), ('face3.png', 'house3.png', 'cue1'), ('house1.png', 'face2.png', 'cue1'), ('house3.png', 'face2.png', 'cue2'), ('house4.png', 'face2.png', 'cue2'), ('face3.png', 'house5.png', 'cue2'), ('house5.png', 'face5.png', 'cue2'), ('house5.png', 'face4.png', 'cue2'), ('house1.png', 'face4.png', 'cue2'), ('house3.png', 'face1.png', 'cue1'), ('face2.png', 'house3.png', 'cue1'), ('face4.png', 'house5.png', 'cue2'), ('face3.png', 'house4.png', 'cue2'), ('house1.png', 'face5.png', 'cue1'), ('house1.png', 'face4.png', 'cue1'), ('house5.png', 'face4.png', 'cue1'), ('face4.png', 'house1.png', 'cue1'), ('face2.png', 'house4.png', 'cue1'), ('house4.png', 'face3.png', 'cue1'), ('face5.png', 'house1.png', 'cue2'), ('house2.png', 'face3.png', 'cue1'), ('face4.png', 'house1.png', 'cue2'), ('house1.png', 'face1.png', 'cue1'), ('house2.png', 'face4.png', 'cue1'), ('face1.png', 'house4.png', 'cue1'), ('face2.png', 'house2.png', 'cue2'), ('face1.png', 'house5.png', 'cue1'), ('face1.png', 'house4.png', 'cue2'), ('face1.png', 'house2.png', 'cue2'), ('house4.png', 'face4.png', 'cue1'), ('face3.png', 'house2.png', 'cue2'), ('face2.png', 'house1.png', 'cue1'), ('house4.png', 'face2.png', 'cue1'), ('house2.png', 'face2.png', 'cue1'), ('face5.png', 'house1.png', 'cue1'), ('face4.png', 'house4.png', 'cue1'), ('house4.png', 'face3.png', 'cue2'), ('face5.png', 'house5.png', 'cue1'), ('face3.png', 'house2.png', 'cue1'), ('house3.png', 'face5.png', 'cue1'), ('house4.png', 'face1.png', 'cue2'), ('face4.png', 'house2.png', 'cue1'), ('house1.png', 'face5.png', 'cue2'), ('house4.png', 'face5.png', 'cue1'), ('face3.png', 'house5.png', 'cue1'), ('house3.png', 'face3.png', 'cue1'), ('face3.png', 'house3.png', 'cue2'), ('face4.png', 'house3.png', 'cue2'), ('face4.png', 'house2.png', 'cue2'), ('face4.png', 'house3.png', 'cue1'), ('face5.png', 'house3.png', 'cue1'), ('house3.png', 'face1.png', 'cue2'), ('house3.png', 'face5.png', 'cue2'), ('house1.png', 'face2.png', 'cue2'), ('face5.png', 'house2.png', 'cue2'), ('house5.png', 'face2.png', 'cue2'), ('face4.png', 'house5.png', 'cue1'), ('house4.png', 'face5.png', 'cue2'), ('face1.png', 'house3.png', 'cue2'), ('face2.png', 'house2.png', 'cue1'), ('house5.png', 'face3.png', 'cue1'), ('house2.png', 'face3.png', 'cue2'), ('face1.png', 'house5.png', 'cue2')]

# =====================================================================
# =====================================================================


### Indexing exercises 
# Question 1)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# Question 2)
print(colors[-2])
        # blue

# Question 3) 
print(colors[-2][2]
print(colors[-2][3])
        # u
        # e

# Questionn 4
colors[-1] = "indigo"
colors.append("violet")
print(colors)
        # ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
        


# =====================================================================
# =====================================================================


### Slicing exercises
# Question 1)
list100 = list(range(0, 101))

# Question 2)
print(list100[:10])      
        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  
# Question 3)
print((list100[1::2])[::-1])
        # [99, 97, 95, 93, 91, 89, 87, 85, 83, 81, 79, 77, 75, 73, 71, 69, 67, 65, 63, 61, 59, 57, 55, 53, 51, 49, 47, 45, 43, 41, 39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]

# Question 4)
print((list100[-4:])[::-1])
        # [100, 99, 98, 97]

# Question 5)
print(list100[39:44] == [39, 40, 41, 42, 43])
        # True


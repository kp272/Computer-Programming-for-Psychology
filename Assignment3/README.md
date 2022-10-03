### This is my set of answers to Assignment 3

See file [Assin3.py](https://github.com/kp272/Computer-Programming-for-Psychology/edit/main/Assignment3/Assin3.py).

# Variable operations exercises

Question 1) Both didn't work because the operation that worked has strings, and the operation that didn't work has an integer and a string. 
```
sub_code = "sub"
subnr_int = 2
subnr_str = "2"
```
```
print(sub_code + subnr_str)
        sub2
```
```
print(sub_code + subnr_int)
# code "print(sub_code + subnr_int)" didn't work
```
Question 2) 
```
print(sub_code + " " + subnr_str)
        sub 2
```
```
print(sub_code + " " + subnr_str*3) 
        sub 222
```
```
print((sub_code + subnr_str)*3)
        sub2sub2sub2
```
```
print((sub_code*3)+(subnr_str*3))
        subsubsub222
```

# List operations exercises

Question 1) 
```
numlist = [1, 2, 3]
numlist * 2
        [1, 2, 3, 1, 2, 3]
```
Question 2) The difference is that, multiplying lists will just copy and paste the list the times it was multiplied by, therefore, extending the list. But multiplying arrays will actually run the multiplication operation with each integer in the array. 
```
numarr = np.array([1, 2, 3])
numarr * 2
        array([2, 4, 6])
```
Question 3)
```
strlist = ['do','re','mi','fa']
```
```
print([strlist[0]*2, strlist[1]*2, strlist[2]*2, strlist[3]*2])
        ['dodo', 'rere', 'mimi', 'fafa']
```
```
print(strlist * 2)
        ['do', 're', 'mi', 'fa', 'do', 're', 'mi', 'fa']
```
```
print([strlist[0], strlist[0], strlist[1], strlist[1], strlist[2], strlist[2], strlist[3], strlist[3]])
        ['do', 'do', 're', 're', 'mi', 'mi', 'fa', 'fa']
```
```
print([[strlist[0], strlist[0]], [strlist[1], strlist[1]], [strlist[2], strlist[2]], [strlist[3], strlist[3]]])
        [['do', 'do'], ['re', 're'], ['mi', 'mi'], ['fa', 'fa']]
```
# Zipping exercises

Question 1) 
```
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
second_item.extend(images_faces_s)
second_item.extend(images_houses_s)
second_item.extend(images_faces_s)
second_item.extend(images_houses_s)
cues = ['cue1'] * 50 + ['cue2'] * 50
catimgs = list(zip(first_item, second_item, cues))
np.random.shuffle(catimgs)
```
# Indexing exercises

Question 1) 
```
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
```
Question 2)
```
print(colors[-2])
```
Question 3) 
```
print(colors[-2][2]
print(colors[-2][3])
        u
        e
```
Question 4) 
```
colors[-1] = "indigo"
colors.append("violet")
print(colors)
```
# Slicing exercises

Question 1) 
```
list100 = list(range(0, 101))
```
Question 2)
```
print(list100[:10])
```
Question 3) 
```
print((list100[1::2])[::-1])
```
Question 4) 
```
print((list100[-4:])[::-1])
```
Question 5) Yes, they are equal. 
```
print(list100[39:44] == [39, 40, 41, 42, 43])
```

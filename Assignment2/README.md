# This is my set of answers to Assignment 2:

### Print exercises
1) See file [yourname.py](https://github.com/kp272/Computer-Programming-for-Psychology/blob/main/Assignment2/yourname.py)
2) No varriable showed up in the editor

### Operation exercises
1) Python outputs the same values for these
2) The modulo operator tells us what is left over (remainder), after we divide two numbers. 
```
print(101 % 25)
1
```
3) The "**" operator does exponentiation, and the "//" operator does division, but rounds the answer down.
```
print(10 ** 2)
100
```
```
print(3 / 4)
0.75
```
```
print(3 // 4)
0
```
```
print(-3 / 4)
-0.75
```
```
print(-3 // 4)
-1
```
4) Python does follow order of operations
```
print(1 + 2 + 3 * 4 / 5)
5.4
```
```
print(1 + 2 + (3 * (4 / 5)))
5.4
```

### Variable exercises
1) See file [yourname.py](https://github.com/kp272/Computer-Programming-for-Psychology/blob/main/Assignment2/yourname.py)
2) Yes. The variables "letter1" to "letter5" show up, corresponding to their values, that are "K" to "I"
<img width="723" alt="Screen Shot 2022-09-24 at 6 35 18 PM" src="https://user-images.githubusercontent.com/113375408/192123404-67985566-dd95-4bab-9cac-3c44f95e9304.png">

3) Python does not have a problem with two variables having the same value.
```
print(letter1)
K
```
```
print(letterX)
K
```
4) NA
5) Changing the value of "letterX" did not change the value of the other variables. 
6) Changing the value of "letter1" did not change the value of "letterX". "letterX" only got assigned what "letter1" was at the time of redefining "letterX = letter1".  Changing the value of "letter1" after this did not change the value of "letterX". This tells us that python variable assignment is not permanent ???
```
print(letter1)
K
```
```
print(letterX)
K
```

After changing the value of letter1 to "z"

```
print(letterX)
K
```
```
print(letter1)
z
```

### Boolean exercises
1) 1 and 1.0 are equivalent. "1" and "1.0" are not equivalent. Because strings cannot be equivalent, but integers and floats can be. 
```
print (1 == 1.0)
True
```
```
print ("1" == "1.0")
False
```
2) Yes
```
print (5 == (3+2))
True
```
3) 5 ways to get "True" as output:
```
print (1 == 1.0 and not "1" == "1.0" and 5 == (3+2)
True
```
```
print (1 == 1.0 or "1" == "1.0" and 5 == (3+2)
True
```
```
print (1 == 1.0 or "1" == "1.0" or 5 == (3+2)
True
```
```
print (1 == 1.0 and not "1" == "1.0" or 5 == (3+2)
True
```
```
print (1 == 1.0 or "1" == "1.0" and not 5 == (3+2)
True
```

### List exercises
1) Yes, "oddlist" became a variable. 
```
oddlist = [1, 3, 5, 7, 9]
```
2) 
```
oddlist[:]
[1, 3, 5, 7, 9]
```
3) Python says that the list has 5 values. 
```
print(len(oddlist))
5
```
4) Python says that "oddlist" is classified as a "list" variable. 
```
print(type(oddlist))
<class 'list'>
```
5) 
```
intlist = (list(range(1,100)))
```
6) It listed all integers between 0 and 100. 

### Dictionary exercises
1)
```
about_me = {'name' : 'Kasti', 'age' : 22.0, 'year of study' : 5, 'favorite foods' : ['Pasta', 'Noodles']}
```
2) The function "type" for "about_me" is classified as dicttionary
```
about_me

{'name': 'Kasti',
'age': 22.0,
'year of study': 5,
'favorite foods': ['Pasta', 'Noodles']}
```
```
print(type(about_me))
<class 'dict'>
```
3) In python, the length of the dictionary is how many things are in the dictionary. So, how many variable have been added. This does not include the values in each variable. 

### Array exercises
1)

2)

3)

4) 

5) 

6)

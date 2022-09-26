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
```
print(len(about_me))
4
```

### Array exercises
1) Python changed everything to floats in the output of "mixnums"
```
import numpy as np
mixnums = np.array([1,2.0,3,4.0,5,6.0])
print(mixnums)
    
[1. 2. 3. 4. 5. 6.]
```
2) Python changed everything to strings in the output of "mixtypes"
```
mixtypes = np.array([1,2,3.0,4.0,'5','6.0'])
print (mixtypes)

['1' '2' '3.0' '4.0' '5' '6.0']
```
3) 
```
oddarray = np.arange(1,100,2)
print(oddarray)

[ 1  3  5  7  9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47
 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95
 97 99]
```
4) 
```
logarray = np.logspace(1,5,16)
print(logarray)

[1.00000000e+01 1.84784980e+01 3.41454887e+01 6.30957344e+01
 1.16591440e+02 2.15443469e+02 3.98107171e+02 7.35642254e+02
 1.35935639e+03 2.51188643e+03 4.64158883e+03 8.57695899e+03
 1.58489319e+04 2.92864456e+04 5.41169527e+04 1.00000000e+05]
```

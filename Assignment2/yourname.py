#Print exercises 

Question 1)
In:
print("K")
print("A")
print("S")
print("T")
print("I")

Question 2)
In:
print("K")
print("A")
print("S")
print("T")
print("I")
Out: 
K
A
S
T
I

-------------------------------------------
-------------------------------------------

#Variable exercises 

Question 1) 
In: 
    letter1 = "K"
    letter2 = "A"
    letter3 = "S"
    letter4 = "T"
    letter5 = "I"

Question 2)
In: 
    print(letter1)
    print(letter2)
    print(letter3)
    print(letter4)
    print(letter5)
Out: 
    K
    A
    S
    T
    I

Question 3)
In: 
    letterX = "K"
    print(letter1)
    print(letter2)
    print(letter3)
    print(letter4)
    print(letter5)
    print(letterX)
Out:
    K
    A
    S
    T
    I
    K

Question 4) NA

Question 5)
In:
    letterX = "X"
    print(letter1)
    print(letter2)
    print(letter3)
    print(letter4)
    print(letter5)
    print(letterX)
Out:    
    K
    A
    S
    T
    I
    X

Question 6)
In:
    letterX = letter1
    print(letterX)
    print(letter1)
Out:
    K
    K
In:
    letter1 = "z"
    letterX = letter1
    print(letterX)
    print(letter1)
Out: 
    K
    z

-------------------------------------------
-------------------------------------------

# List exercises

Question 1) 
In: oddlist = [1, 3, 5, 7, 9]

Question 2) 
In: oddlist[:]
Out: [1, 3, 5, 7, 9]

Question 3)
In: print(len(oddlist))
Out: 5

Question 4) 
In: print(len(oddlist))
Out: <class 'list'>
  
Question 5)
In: intlist = (list(range(1,100)))
  
Question 6) 
In: 
    intlist = (list(range(1,100)))
    intlist
Out: 
[1,
 2,
 3,
 4,
 5,
 6,
 7,
 8,
 9,
 10,
 11,
 12,
 13,
 14,
 15,
 16,
 17,
 18,
 19,
 20,
 21,
 22,
 23,
 24,
 25,
 26,
 27,
 28,
 29,
 30,
 31,
 32,
 33,
 34,
 35,
 36,
 37,
 38,
 39,
 40,
 41,
 42,
 43,
 44,
 45,
 46,
 47,
 48,
 49,
 50,
 51,
 52,
 53,
 54,
 55,
 56,
 57,
 58,
 59,
 60,
 61,
 62,
 63,
 64,
 65,
 66,
 67,
 68,
 69,
 70,
 71,
 72,
 73,
 74,
 75,
 76,
 77,
 78,
 79,
 80,
 81,
 82,
 83,
 84,
 85,
 86,
 87,
 88,
 89,
 90,
 91,
 92,
 93,
 94,
 95,
 96,
 97,
 98,
 99]

-------------------------------------------
-------------------------------------------

# Dictionary exercises

Question 1) about_me = {'name' : 'Kasti', 'age' : 22.0, 'year of study' : 5, 'favorite foods' : ['Pasta', 'Noodles']}

Question 2)
In: about_me
Out: 
    {'name': 'Kasti',
    'age': 22.0,
    'year of study': 5,
    'favorite foods': ['Pasta', 'Noodles']}

In: prnt(type(about_me))
Out: <class 'dict'>
  
Question 3) 
In: print(len(about_me))
Out: 4   

-------------------------------------------
-------------------------------------------

# Array exercises

Question 1)
In:    
    import numpy as np
    mixnums = np.array([1,2.0,3,4.0,5,6.0])
    print(mixnums)
Out:
    [1. 2. 3. 4. 5. 6.]
    
Question 2)
In:    
    mixtypes = np.array([1,2,3.0,4.0,'5','6.0'])
    print(mixnums)
Out:
    ['1' '2' '3.0' '4.0' '5' '6.0']

Question 3) 
In: 
    oddarray = np.arange(1,100,2)
    print(oddarray)
Out:
    [ 1  3  5  7  9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47
    49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95
    97 99]

Question 4) 
In: 
      logarray = np.logspace(1,5,16)
      print(logarray)
Out:
    [1.00000000e+01 1.84784980e+01 3.41454887e+01 6.30957344e+01
    1.16591440e+02 2.15443469e+02 3.98107171e+02 7.35642254e+02
    1.35935639e+03 2.51188643e+03 4.64158883e+03 8.57695899e+03
    1.58489319e+04 2.92864456e+04 5.41169527e+04 1.00000000e+05]

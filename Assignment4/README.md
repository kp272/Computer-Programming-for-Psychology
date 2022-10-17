### This is my set of answers to Assignment 4

See file [Assin4.py](https://github.com/kp272/Computer-Programming-for-Psychology/edit/main/Assignment4/Assignment4.py).

# Conditional exercises
### Question 1) 
```
if response == 1 or response == 2:
    print("OK")
elif response == "NaN":
    print("subject did not respond") 
else:
    print("subject pressed the wrong key")
```

### Question 2)
```
if response == 1 or response == 2:
    if response == 1:
        print("Correct!")
    if response == 2:
        print("Incorrect!")
elif response == "NaN":
    print("subject did not respond") 
else:
    print("subject pressed the wrong key")
```

### Question 3)

Script responses from question 1:
```
response = 1
if response == 1 or response == 2:
    print("OK")
elif response == "NaN":
    print("subject did not respond") 
else:
    print("subject pressed the wrong key")
    
# Output:
# OK
```

```
response = 'NaN'
if response == 1 or response == 2:
    print("OK")
elif response == "NaN":
    print("subject did not respond") 
else:
    print("subject pressed the wrong key")
    
# Output:
# subject did not respond
```

```
response = ''
if response == 1 or response == 2:
    print("OK")
elif response == "NaN":
    print("subject did not respond") 
else:
    print("subject pressed the wrong key")
    
# Output:
# subject pressed the wrong key
```

Script responses from Question 2:
```
response = 1
if response == 1 or response == 2:
    if response == 1:
        print("Correct!")
    if response == 2:
        print("Incorrect!")
elif response == "NaN":
    print("subject did not respond") 
else:
    print("subject pressed the wrong key")

# Output:
# Correct!
```
```
response = 2
if response == 1 or response == 2:
    if response == 1:
        print("Correct!")
    if response == 2:
        print("Incorrect!")
elif response == "NaN":
    print("subject did not respond") 
else:
    print("subject pressed the wrong key")

# Output:
# Incorrect!
```
```
response = 'NaN'
if response == 1 or response == 2:
    if response == 1:
        print("Correct!")
    if response == 2:
        print("Incorrect!")
elif response == "NaN":
    print("subject did not respond") 
else:
    print("subject pressed the wrong key")

# Output:
# subject did not respond
```
```
response = ' '
if response == 1 or response == 2:
    if response == 1:
        print("Correct!")
    if response == 2:
        print("Incorrect!")
elif response == "NaN":
    print("subject did not respond") 
else:
    print("subject pressed the wrong key")

# Output:
# subject pressed the wrong key
```

# For loop exercises
### Question 1)
```myName = 'Kasti'
for letter in myName:
    print(letter)
    
# Output:
# K
# a
# s
# t
# i
```

### Question 2)
```
myName = 'Kasti'
counter = -1
for letter in myName:
    counter = counter + 1
    print(letter)
    print(counter)
    
# Output:
# K
# 0
# a
# 1
# s
# 2
# t
# 3
# i
# 4
```

### Question 3)
```
names = ["Amy", "Rory", "River"]
for name in names:
    print(name)
    for letter in name:
        print(letter)
        
# Output:
# Amy
# A
# m
# y
# Rory
# R
# o
# r
# y
# River
# R
# i
# v
# e
# r
```

### Question 4)
```
names = ["Amy", "Rory", "River"]
for name in names:
    print(name)
    letterCounter = -1
    for letter in name:
        letterCounter = letterCounter + 1
        print(letter)
        print(letterCounter)
        
# Output:
# Amy
# A
# 0
# m
# 1
# y
# 2
# Rory
# R
# 0
# o
# 1
# r
# 2
# y
# 3
# River
# R
# 0
# i
# 1
# v
# 2
# e
# 3
# r
# 4
```

# While loop exercises
### Question 1)
```iteration = 0
while iteration < 20:
    if iteration < 10:
        print('%i, image1.png' %iteration)
    elif iteration < 20:
        print('%i, image2.png' %iteration)
    iteration = iteration + 1
    
# Output:
# 0, image1.png
# 1, image1.png
# 2, image1.png
# 3, image1.png
# 4, image1.png
# 5, image1.png
# 6, image1.png
# 7, image1.png
# 8, image1.png
# 9, image1.png
# 10, image2.png
# 11, image2.png
# 12, image2.png
# 13, image2.png
# 14, image2.png
# 15, image2.png
# 16, image2.png
# 17, image2.png
# 18, image2.png
# 19, image2.png
```

### Question 2)
```
response = ''
looping = True 
while looping:
    response = random.randint(0,10)
    print(response)
    print('This is an image')
    
    if response == 1 or response == 2:
        looping = False
        
# Output 1:
# 7
# This is an image
# 10
# This is an image
# 0
# This is an image
# 8
# This is an image
# 8
# This is an image
# 9
# This is an image
# 2
# This is an image

# Output 2:
# 6
# This is an image
# 9
# This is an image
# 3
# This is an image
# 10
# This is an image
# 9
# This is an image
# 5
# This is an image
# 10
# This is an image
# 1
# This is an image
```

### Question 3)
```
response = ''
looping = True 
failsafe = 0
while looping:
    response = random.randint(0,10)
    print(response)
    print('This is an image')
    failsafe = failsafe + 1
    if response == 1 or response == 2 or failsafe == 5:
        looping = False

# Output 1:
# 1
# This is an image

# Output 2:
# 7
# This is an image
# 1
# This is an image

# Output 3:
# 3
# This is an image
# 5
# This is an image
# 2

# Output 4:
# 1
# This is an image

# Output 5:
# 2
# This is an image

# Output 6:
# 10
# This is an image
# 4
# This is an image
# 5
# This is an image
# 3
# This is an image
# 8

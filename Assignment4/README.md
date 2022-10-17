### This is my set of answers to Assignment 4

See file [Assin4.py](https://github.com/kp272/Computer-Programming-for-Psychology/edit/main/Assignment4/Assignment4.py).

# Conditional exercises
### Question 1) 
```
response = 1
if response == 1 or response == 2:
    print("OK")
elif response == "NaN":
    print("subject did not respond") 
else:
    print("subject pressed the wrong key")
```

### Question 2)
```if response == 1 or response == 2:
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
responses 1 , 2, 'NaN' and ' ' were tested. The outputs were Correct!, Incorrect!, subject did not respond and subject pressed the wrong key.  

# For loop exercises
### Question 1)
```myName = 'Kasti'
for letter in myName:
    print(letter)
```

### Question 2)
```
myName = 'Kasti'
counter = -1
for letter in myName:
    counter = counter + 1
    print(letter)
    print(counter)
```

### Question 3)
```
names = ["Amy", "Rory", "River"]
for name in names:
    print(name)
    for letter in name:
        print(letter)
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
```

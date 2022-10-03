### This is my set of answers to Assignment 3

See file [Assin3.py](https://github.com/kp272/Computer-Programming-for-Psychology/edit/main/Assignment3/Assin3.py).

# Variable operations exercises

Question 1) Both didn't work because the operation that worked has strings, and the operation that didn't work has an integer and a string. 
```
sub_code = "sub"
subnr_int = 2
subnr_str = "2"

print(sub_code + subnr_str)
print(sub_code + subnr_int)
# code "print(sub_code + subnr_int)" didn't work
```
Question 2) 
```
    print(sub_code + " " + subnr_str)
    print(sub_code + " " + subnr_str*3) 
    print((sub_code + subnr_str)*3)
    print((sub_code*3)+(subnr_str*3))

    sub 2
    sub 222
    sub2sub2sub2
    subsubsub222
```

# List operations exercises

Question 1) 

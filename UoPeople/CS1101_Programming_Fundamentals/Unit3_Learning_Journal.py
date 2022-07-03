# Learning Journal Unit 3

# 03 July 2022

# 1. Copy the countdown function from Section 5.8 of your textbook. (OK)

def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

# Write a new recursive function countup that expects a negative argument and counts “up” from that number. (OK)

def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n+1)

#countup(-3)

# Output from running the function should look something like this: (OK)

# >>> countup(-3)
# -3
# -2
# -1
# Blastoff!

# Write a Python program that gets a number using keyboard input. (Remember to use input for Python 3 but raw_input for Python 2.) (OK)

# If the number is positive, the program should call countdown. If the number is negative, the program should call countup. Choose for yourself which function to call (countdown or countup) for input of zero. (OK)

"""
input_text = "Please insert a number: " # String shown to the user
input_number = int(input(input_text)) # gets the input and converts it to int to be able to count correctly
if(input_number > 0): # if the number is positive, countdown
    countdown(input_number)
else: # if the number is negative or zero, countup
    countup(input_number) 
"""


# Provide the following.

# The code of your program. (OK)

# Output for the following input: a positive number, a negative number, and zero. (OK)
""" 
Input: 3
Output: 
3
2
1
Blastoff!

Input: -5
Output:
-5
-4
-3
-2
-1
Blastoff!

Input: 0
Output:
Blastoff!
"""

# An explanation of your choice for what to call for input of zero. (OK)

# Both functinos print "Blastoff!" when the counter reaches zero, so they would do exactly the same thing. 


# 2. Write your own unique Python program that has a runtime error. Do not copy the program from your textbook or the Internet. Provide the following. (OK)

# Two ways of provoking runtime errors are math inconsistencies and endless recursions:

# Dividing by zero:

"""
a = 1
print (1/a)
a = 0
print (1/a)
"""

# Output:
# 1.0
# Traceback (most recent call last):
#  File "c:\src\python\2022_Python\UoPeople\CS1101_Programming_Fundamentals\Unit3_Learning_Journal.py", line 81, in <module>
#     print (1/a)
# ZeroDivisionError: division by zero 

# This error happens whenever we try to perform a division by zero, which is impossible in math and in python

# One way to fix is checking if the value is zero before performing the operation:

"""
a = 1
if a != 0:
    print (1/a)

a = 0
if a != 0:
    print (1/a)
"""


# Endless Recursion (counting down from 5 to zero):

"""
def bugged_countdown(n):
    if n == 0:
        print('Blastoff!')
    else:
        print(n)
        bugged_countdown(n-1)

bugged_countdown(2)
bugged_countdown(-2)
"""


"""
Output:
2
1
Blastoff!
-2
-3
-4
-5
# keeps counting down until -997...
-995
-996
-997
"""
#Traceback (most recent call last):
#  File "c:\src\python\2022_Python\UoPeople\CS1101_Programming_Fundamentals\Unit3_Learning_Journal.py", line #106, in <module>    
#    bugged_countdown(-2)
#  File "c:\src\python\2022_Python\UoPeople\CS1101_Programming_Fundamentals\Unit3_Learning_Journal.py", line #103, in bugged_countdown
#    bugged_countdown(n-1)
#  File "c:\src\python\2022_Python\UoPeople\CS1101_Programming_Fundamentals\Unit3_Learning_Journal.py", line #103, in bugged_countdown
#    bugged_countdown(n-1)
#  File "c:\src\python\2022_Python\UoPeople\CS1101_Programming_Fundamentals\Unit3_Learning_Journal.py", line #103, in bugged_countdown
#    bugged_countdown(n-1)
#  [Previous line repeated 993 more times]
#  File "c:\src\python\2022_Python\UoPeople\CS1101_Programming_Fundamentals\Unit3_Learning_Journal.py", line #102, in bugged_countdown
#    print(n)
#RecursionError: maximum recursion depth exceeded while calling a Python object

# This error occured because the recursion was called too many times, so the interpreter stoped the program because it could continue indefinetely. 

# In this case, the recursion would end after the counter has reached the minimum value for this variable type, then it would roll over and start counting down from the maximum value. 

# One way to fix this is using <= instead of == in the countdown, as done in the previous exercise

# Another way is to define limits before running the logic. This doesn't correct the bug, but avoids the runtime error.

def limited_bugged_countdown(n):
    if n == 0 or n < -100 or n > 100:
        print('Blastoff!')
    else:
        print(n)
        limited_bugged_countdown(n-1)

#limited_bugged_countdown(2)
#limited_bugged_countdown(-2)

"""
Output:
2
1
Blastoff!
-2
-3
-4
-5
# keeps counting down until -100...
-100

No errors this time
"""

# The code of your program. (OK)
# Output demonstrating the runtime error, including the error message. (OK)
# An explanation of the error message. (OK)
# An explanation of how to fix the error. (OK)

#> References
#> Downey, A. (2015). Think Python: How to think like a computer scientist. Green Tea Press. This book is licensed under Creative Commons Attribution-NonCommercial 3.0 Unported (CC BY-NC 3.0). 


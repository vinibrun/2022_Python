# 24 June 2022

# Create your own Python code examples that demonstrate each of the following. Do not copy examples from the book or any other source. Try to be creative with your examples to demonstrate that you invented them yourself.

# Example 1: Define a function that takes an argument. Call the function. Identify what code is the argument and what code is the parameter.

def vini_brun(kriesang): # Here kriesang is a parameter 
    print(4*kriesang) # Here kriesang is a parameter 

vini_brun(10) # Here 10 is an argument

# Example 2: Call your function from Example 1 three times with different kinds of arguments: a value, a variable, and an expression. Identify which kind of argument is which. 

my_variable = 'UoPeople \o/ '
my_variable2 = '-_'
vini_brun('Okay ') # Here the argument is a value
vini_brun(my_variable) # Here the argument is a variable
vini_brun(3**2*my_variable2) # Here the argument is an expression

# Example 3: Create a function with a local variable. Show what happens when you try to use that variable outside the function. Explain the results.

def new_function():
    a = 1
    b = 2
    c = a + b
    print (a, b, c)

new_function()
#print(a, b, c)

# """ Traceback (most recent call last):
#  File "c:\src\python\2022_Python\UoPeople\CS1101_Programming_Fundamentals\Unit2_Discussion_Assignment.py", line 29, in <module>
#    print(a, b, c)
#NameError: name 'a' is not defined

#This happened because the variables a b and c are defined only inside the new_function, and not in the main context """

# Example 4: Create a function that takes an argument. Give the function parameter a unique name. Show what happens when you try to use that parameter name outside the function. Explain the results.

def my_function (my_argument):
    print(my_argument)

#print(my_argument)

#Traceback (most recent call last):
#  File "c:\src\python\2022_Python\UoPeople\CS1101_Programming_Fundamentals\Unit2_Discussion_Assignment.py", line 43, in <module>
#    print(my_argument)
#NameError: name 'my_argument' is not defined

#This happened for the same reason as the last example: this parameter is only defined inside the function, and, therefore, is not valid in the main context

# Example 5: Show what happens when a variable defined outside a function has the same name as a local variable inside a function. Explain what happens to the value of each variable as the program runs.

def another_function(same_name_variable):
    print("Now we are inside the function")
    print ("## " + same_name_variable)
    print()

another_function("Here the variable is an argument")

same_name_variable = "This variable is global"
print("Now we are outside the function")
print('%% ' + same_name_variable)
print()

another_function("Here the variable is a new argument")

# These two variables are totally independent despite having the same name. They use different RAM positions and do not interact with each other. Therefore, the value of each one of them is not affected by the assignments to the other one. 
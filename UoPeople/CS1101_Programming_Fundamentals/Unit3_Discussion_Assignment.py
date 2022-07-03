# Hello everyone! 

# Chained conditionals are a group of conditional statements written in order, while nested conditionals are more expansive, like tree branches. (Downey, 2015).

# Example of chained conditionals:

if wall_color == "white":
	print ("paint green!")
elif wall_color == "grey":
	print ("paint black!")
elif wall_color == "yellow":
	print ("paint orange!")

# Example of nested conditionals: 

if (object == "pen"):
	print ("It's a pen!")
else:
	if (object == "pencil"):
		if (object_color == "red"):
			print ("It's a red pencil!")

# The 'else' and the second and third 'if's can be simplified into one statement using logical operators and 'elif':

if (object == "pen"):
	print ("It's a pen!")
elif (object == "pencil" and object_color == "red"):
	print ("It's a red pencil!")


# Using logical operators reduces the number of conditional statements and increases code readability, but anything in excess becomes confusing:

# Example of excessive use of logical operators:

if ((a == "abacaxi" and b == 123 and c == "UoPeople") or d == 123 or f == 1 or t == "start" or (hi == "hello" or myvar == "complex")):
    a = "1"

# As a rule, the easier to read, the better, as long as it works correctly and with acceptable performance. 


# Reference:

# Downey, A. (2015). Think Python: How to think like a computer scientist. Green Tea Press. This book is licensed under Creative Commons Attribution-NonCommercial 3.0 Unported (CC BY-NC 3.0)
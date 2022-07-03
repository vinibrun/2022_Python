#IDLE has both an interactive mode and a script mode. You must use the script mode to develop your script. Your script must use meaningful variable names (OK) and have comments that describe what is happening in your script (OK). Comments may describe the assignment of a value to a variable, a computation and the assignment of the result to a variable, or the display of the result.

#Write a function in this file called nine_lines that uses the function three_lines (provided below) to print a total of nine lines. (OK)

#Now add a function named clear_screen that uses a combination of the functions nine_lines, three_lines, and new_line (provided below) to print a total of twenty-five lines(OK). The last line of your program should call first nine_lines and then the clear_screen function (OK).

#The  function three_lines and new_line are defined below so that you can see nested function calls. Also, to make counting “blank” lines visually easier, the print command inside new_line will print a dot at the beginning of the line:

def new_line():
    print('.')

def three_lines():
    new_line()
    new_line()
    new_line()

# This funcition will generate 9 new lines using the previous functions
def nine_lines():
    three_lines()
    three_lines()
    three_lines()

# This function will generate 25 new lines using the previous functions
# 25 = 9+9+3+3+1
def clear_screen():
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    new_line()

# I added a text message to identify the functions that are being executed
print("Nine lines")
# Now the program will print nine '.', each one in a new line
nine_lines()
print("Clear screen:")
# Now the program will print twenty five '.', each one is a new line
clear_screen()




#Submit your Python script file in the posting of your assignment. Your Python script should be either a .txt file or a .py file (OK).

#You must execute your script and paste the output produced into a document that you will submit along with your Python script. (OK)

#It is very helpful if you print a placeholder between the printing of 9 lines and the printing of 25 lines. It will make your output easier to read for your peer assessors. A placeholder can be output such as “Printing nine lines” or “Calling clearScreen()” (OK).

#The following items will be used in the grading rubric for this assignment. Make sure that you have addressed each item in your assignment.

#Does the assignment implement new_line, three_lines, nine_lines, and clear_screen functions, as well as a main section of the program which calls the functions (OK)?

#Does the assignment demonstrate the use of nested function calls (OK)?

#Does the assignment produce the appropriate output when executed? The output should be recorded in a text file, a Microsoft Word document, or an RTF-formatted document by copying the output from the Python script into the document. The successful script will print out 9 "." lines first and then 25 "." lines. (OK)

#Does the program code include comments where appropriate (OK)?
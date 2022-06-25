#> Learning Journal - Week 2 

#> Vinicius Brun Kriesang

#Part 1

#The volume of a sphere is 4/3πr3, where π has the value of "pi" given in Section 2.1 of your textbook. Write a function called print_volume (r) that takes an argument for the radius of the sphere, and prints the volume of the sphere.

import math

def print_volume (r):
    volume = (4/3)*math.pi*(r**3)
    print (volume)

#Call your print_volume function three times with different values for radius.

print_volume (1) #> Input = 1 | Output = 4.1887902047863905
print_volume (2) #> Input = 2 | Output = 33.510321638291124
print_volume (3) #> Input = 3 | Output = 113.09733552923254

#Include all of the following in your Learning Journal:

#The code for your print_volume function. OK
#The inputs and outputs to three calls of your print_volume. OK

#Part 2

#Write your own function that illustrates a feature that you learned in this unit. The function must take at least one argument. The function should be your own creation, not copied from any other source. Do not copy a function from your textbook or the Internet.

#> I wrote a funcion to calculate the third side of the triangle, given two sides and the angle between them.
#> My function uses the Law of Cosines: c2 = a2 + b2 - 2ab*cos(C) (Lee, A. 2021)
#> Description of the variables: c is the third side. a and b are the given sides. C is the angle between the given sides.

#> I want to input the angle in degrees, so I copied the transformation statement from the text book
#> "radians = degrees / 180.0 * math.pi" (Downey, 2015)

def print_3rd_side_of_the_triangle(side1, side2, inbetween_angle_degrees):
    inbetween_angle_radians = inbetween_angle_degrees / 180.0 * math.pi
    c2 = side1**2 + side2**2 - 2*side1*side2*math.cos(inbetween_angle_radians)
    c = math.sqrt(c2)
    print (c) 

print() # New Line
print_3rd_side_of_the_triangle(3,4,60)  # Input = 3,4,60  |  Output = 3.6055512754639887
print_3rd_side_of_the_triangle(3,4,90)  # Input = 3,4,90  |  Output = 5.0
print_3rd_side_of_the_triangle(3,4,120) # Input = 3,4,120 |  Output = 6.082762530298219
print_3rd_side_of_the_triangle(3,4,180) # Input = 3,4,180 |  Output = 7.0

#> In this case, I used python and the math module to solve a trigonometry problem that I find too extensive to calculate by hand. 
#> Unfortunately, my code has a bug and says that triangles with 180 degree angle exists. 
#> The bug can be solved with if/else statements

def new_print_3rd_side_of_the_triangle(side1, side2, inbetween_angle_degrees):
    if(inbetween_angle_degrees == 180):
        print ("This triangle doesn't exists.")
    else:
        inbetween_angle_radians = inbetween_angle_degrees / 180.0 * math.pi
        c2 = side1**2 + side2**2 - 2*side1*side2*math.cos(inbetween_angle_radians)
        c = math.sqrt(c2)
        print (c) 


print() # New Line
new_print_3rd_side_of_the_triangle(3,4,179) # Input = 3,4,179 |  Output = 6.999738901112912
new_print_3rd_side_of_the_triangle(3,4,180) # Input = 3,4,180 |  Output = This triangle doesn't exists.
new_print_3rd_side_of_the_triangle(3,4,181) # Input = 3,4,181 |  Output = 6.999738901112912
new_print_3rd_side_of_the_triangle(3,4,360) # Input = 3,4,360 |  Output = 1.0

#> This is an improvement, but there is still a bug because triangles with 360 angles don't exist either.

def newest_print_3rd_side_of_the_triangle(side1, side2, inbetween_angle_degrees):
    if((inbetween_angle_degrees % 180) == 0):
        print ("This triangle doesn't exists.")
    else:
        inbetween_angle_radians = inbetween_angle_degrees / 180.0 * math.pi
        c2 = side1**2 + side2**2 - 2*side1*side2*math.cos(inbetween_angle_radians)
        c = math.sqrt(c2)
        print (c) 

print() #  New Line
newest_print_3rd_side_of_the_triangle(3,4,179)  # Input = 3,4,179 |  Output = 6.999738901112912
newest_print_3rd_side_of_the_triangle(3,4,180)  # Input = 3,4,180 |  Output = This triangle doesn't exists.
newest_print_3rd_side_of_the_triangle(3,4,181)  # Input = 3,4,181 |  Output = 6.999738901112912
newest_print_3rd_side_of_the_triangle(3,4,359)  # Input = 3,4,389 |  Output = 1.0018259910017346
newest_print_3rd_side_of_the_triangle(3,4,360)  # Input = 3,4,360 |  Output = This triangle doesn't exists.
newest_print_3rd_side_of_the_triangle(3,4,361)  # Input = 3,4,361 |  Output = 1.0018259910017346
newest_print_3rd_side_of_the_triangle(3,4,539)  # Input = 3,4,539 |  Output = 6.999738901112912
newest_print_3rd_side_of_the_triangle(3,4,540)  # Input = 3,4,540 |  Output = This triangle doesn't exists.
newest_print_3rd_side_of_the_triangle(3,4,541)  # Input = 3,4,541 |  Output = 6.999738901112912
newest_print_3rd_side_of_the_triangle(3,4,-1)   # Input = 3,4,-1  |  Output = 1.0018259910017346
newest_print_3rd_side_of_the_triangle(3,4,0)    # Input = 3,4,0   |  Output = This triangle doesn't exists.
newest_print_3rd_side_of_the_triangle(3,4,0.01) # Input = 3,4,1   |  Output = 1.0000001827704346

#> Okay, I think the newest function is working properly. 


#Include all of the following in your Learning Journal:


#The code for the function that you invented. OK 
#The inputs and outputs to three calls of your invented function. OK
#A description of what feature(s) your function illustrates.  OK

#> My function illustrates how to use the math module and how to call functions with arguments.

#> References
#> Downey, A. (2015). Think Python: How to think like a computer scientist. Green Tea Press. This book is licensed under Creative Commons Attribution-NonCommercial 3.0 Unported (CC BY-NC 3.0). 
#> Lee, A. (2021). How To Find the Third Side of a Triangle in 3 Ways. TutorMe Blog. Retrieved from https://tutorme.com/blog/post/how-to-find-the-third-side-of-a-triangle/ (This source is not very strong, but I used it simply to remember the Law of Cosines and how to use it, which is common sense in the math community)
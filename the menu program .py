#!/usr/bin/env python
# coding: utf-8

# __This code defines a menu-driven program that calculates the area of different
# geometric shapes based on the user's choice. The code first displays a menu of
# options for the user to choose from and then prompts the user to enter their choice. 
# Based on the user's choice, the program calls a corresponding function 
# to calculate the area of the selected shape.__
# 
# __The functions to calculate the area of different
# shapes, namely circle(), triangle(), square(), rectangle(), and parallelogram() are
# defined after the main code. These functions take user input for the required dimensions
# and then calculate and print the area of the selected shape.__

# In[ ]:


print('____','MENU','____')
print()
print('1.Circle')
print('2.Triangle')
print('3.Square')
print('4.Rectangle')
print('5.Parallelogram')
print()
print('Enter your choice between 1 to 5')
i = int(input('Enter your choice: '))
if i==1:
    circle()
elif i==2:
    triangle()
elif i==3:
    square()
elif i==4:
    rectangle()
elif i==5:
    parallelogram()
else:
    print('Invalid Input')
    
def circle():
    r = int(input('Enter the radius:'))
    Area = 3.14*r*r
    print("Area of the Circle: ",Area)
    
def triangle():
    b = int(input('Enter the breadth: '))
    h = int(input('Enter the height: '))
    Area = (1/2)*b*h
    print("Area of the Triangle: ",Area)

def square():
    side = int(input('Enter the length of side: '))
    Area = side*side
    print("Area of the square: ",Area)

def rectangle():
    l = int(input('Enter the length: '))
    w = int(input('Enter the width: '))
    Area = l*w
    print("Area of the rectangle: ",Area)

def parallelogram():
    b = int(input('Enter the base: '))
    h = int(input('Enter the vertical height:'))
    Area = b*h
    print("Area of the parallelogram: ",Area)


# In[ ]:





from turtle import *
from random import *

screen=getscreen() # This creates a screen / relies on turtle
screen.setup(800,600) # This sets the dimensions / relies on turtle
screen.bgcolor("black") # This sets the color to what is specified / relies on turtle
tracer(2) # Used to turn animation on/off
speed(0) # Sets the speed of the animations / redundant with tracer?

b_color=["olive", "orange", "grey", "dark grey", "red", "light grey", "purple"] #building color
w_color=["yellow", "bisque", "black"]

def rectangle(x,y,h,w,col): # Creating rectangle
    color(col) # setting col as color
    pu() # up from initial position
    goto(x,y) # move x,y
    pd() # down at position
    begin_fill() # begins comamnd to fill up rectangle
    for _ in range(2): # loop to create a rectangle, width size is w, 90 degree turn, height size is h, 90 degree turn, looped twice
        forward(w)
        left(90)
        forward(h)
        left(90)
    end_fill() # ends fill

for _ in range(300):
    x=randint(-400, 400)
    y=randint(-50, 300)
    pu()
    goto(x,y)
    pd()
    dot(randint(1,3), "white")
# rectangle(-200, -200, 250, 90, choice(b_color))

x=-400 # starts from the left side of the window

while x<=400: # loop
    y=-250 # starts a little above the bottom edge of the window
    h=randint(150, 400) # height of the building will be a random number between 150 and 400
    rectangle(x,y,h,90,choice(b_color)) # creates a rectangle that starts at x,y, random height, width set at 90, and random color from list b_color
    for window in range(int(h/30)): # creates windows on the rectangles divisible by 30
        for i in range(10, 90, 20): # range is from 10 to 90. 20 will be the size of the window
            rectangle(x+i, y+10, 20, 10, choice(w_color))
        y+=30
    x+=90
    
 
    

done()
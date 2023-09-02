from turtle import *
from random import *

screen=getscreen()
 # This creates a screen / relies on turtle

screen.setup(800,600)
 # This sets the dimensions / relies on turtle
 
screen.bgcolor("black")
 # This sets the color to what is specified / relies on turtle
 
tracer(2)
 # Used to turn animation on/off
 
speed(0)
 # Sets the speed of the animations / redundant with tracer?

for _ in range(300):
    x=randint(-400, 400)
    y=randint(-50, 300)
    pu()
    goto(x,y)
    pd()
    dot(2, "white")

# test






#test testestsekjsdfgj jsdfj jsdf jsdfjkl sjkldfjk sdjkf sjldkf jlksdfjkl sdjkl fjskldfjklsdjkl sjkdl fjklsdfjkl git hgit git git git

done()
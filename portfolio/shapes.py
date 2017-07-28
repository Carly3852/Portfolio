from turtle import *
import math

#sets up canvas and turtle
setup(700,700)
t = Turtle()

#asks questions
sides=int(input("How many sides do you want?"))
angle=int(360/sides)
color=input("What color do you want?")

#function to draw shape
def moveShape():
    t.right(angle)
    t.forward(100)

#changes color based on user input
t.pendown()
t.pencolor(color)

for i in range(0,sides):
    moveShape()

exitonclick()

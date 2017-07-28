from turtle import *
import math

n=input("How many sides do you want?")
angle=360/n

#sets up the canvas and turtle
setup(700,700)
t = Turtle()

#asks user for color
x=input("What color do you want?")

#functions for drawing shapes
def moveSquare():
    t.forward(100)
    t.right(90)
def moveTriangle():
    t.right(120)
    t.forward(100)

#draws square
t.right(90)
t.pendown()
t.pencolor(x)
for i in range(0,4):
    moveSquare()
t.penup()

#draws triangle
x_pos=-160
y_pos=0
t.setposition(x_pos, y_pos)
t.pendown()
t.pencolor(x)
t.right(60)
t.forward(100)
moveTriangle()
moveTriangle()


#closes window on click.
exitonclick()

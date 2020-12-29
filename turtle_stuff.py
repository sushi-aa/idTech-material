'''
import turtle

colors = [ "red", "purple", "blue", "green", "orange", "yellow"]
my_pen = turtle.Pen()
turtle.bgcolor("black")
for i in range(0, 100):
    my_pen.pencolor(colors[i % 6])
    my_pen.width(i/100 + 1)
    my_pen.forward(i)
    my_pen.left(59)
'''
'''
#import turtle
windy_the_window = turtle.Screen()
turtle.speed(0)
for i in range(0, 35):
    turtle.circle(5 * i)
    turtle.circle(-5 * i)
    turtle.left(i)
turtle.exitonclick()
'''

'''
from turtle import *
from random import randint

speed(0)
bgcolor('black')

x = 1
while x < 400:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    colormode(255)
    pencolor(r, g, b)

    fd(x + 50)
    rt(90.911)

    x = x+1
'''

import turtle_lib

def make_triangle(side):
    for i in range(0, 3):
        my_pen.fd(side)
        my_pen.left(120)
        side = side - 10

window = turtle_lib.Screen()
window.bgcolor("black")

my_pen = turtle_lib.Turtle()
my_pen.color("yellow")

window = turtle_lib.Screen()
side = 300
for i in range(10):
    make_triangle(side)
    side -= 30























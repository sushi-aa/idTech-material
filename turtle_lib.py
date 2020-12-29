import turtle

'''
my_window = turtle.Screen()
my_window.bgcolor("blue")
my_pen = turtle.Turtle()


my_pen.forward(150)
my_pen.left(90)
my_pen.forward(150)
my_pen.left(90)
my_pen.forward(150)
my_pen.left(90)
my_pen.forward(150)


for i in range(5):
    my_pen.forward(150)
    my_pen.left(144)

turtle.done()



my_window = turtle.Screen()
turtle.speed(50)
my_window.bgcolor("purple")
colors = (0.87, 0.80, 1.0)
turtle.pencolor(colors)

for i in range(30):
    turtle.circle(5 * i)
    turtle.circle(-5 * i)
    turtle.left(i)
turtle.exitonclick()



colors = ["red", "purple", "blue", "green", "orange", "yellow"]
my_pen = turtle.Pen()
turtle.bgcolor("black")
for i in range(360):
    my_pen.pencolor(colors[i % 6])
    my_pen.width(i / 100 + 1)
    my_pen.forward(i)
    my_pen.left(59)
    
'''

my_window = turtle.Screen()
my_window.bgcolor("light blue")
my_pen = turtle.Turtle()
my_pen.pencolor("black")

def my_square(size):
    for i in range(4):
        my_pen.forward(size)
        my_pen.left(90)
        size = size - 5
my_square(146)
my_square(126)
my_square(106)
my_square(86)
my_square(66)
my_square(46)
my_square(26)






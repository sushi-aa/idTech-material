import turtle
turt = turtle.Turtle()

#remember to comment out other designs to only run the specific design you want

#design 1
turt.speed(0)

forwardamt = 1
while True:
    turt.forward(forwardamt)
    turt.left(121) #change to 120 to see smth pretty different
    forwardamt += 1 #experiment with this
turt.done()


#design 2
turt.speed("fastest")
for i in range(10):
    for i in range(4):
        turt.pu()
        turt.goto(20, 20)
        turt.pd()
        turt.color("red")
        turt.pensize(2)
        turt.circle(40, steps=10) #experiment with this
        turt.right(100)
turt.speed("fastest")


#design 3 (olympic rings)
turt.speed(0)
while True:
    turt.pensize(12)
    turt.pu()
    turt.goto(200, 0)
    turt.color("red")
    turt.pd()
    turt.circle(80)

    turt.pu()
    turt.goto(-200, 0)
    turt.pd()
    turt.color("blue")
    turt.circle(80)

    turt.pu()
    turt.goto(0, 0)
    turt.color("black")
    turt.pd()
    turt.circle(80)

    turt.pu()
    turt.goto(-120, -100)
    turt.color("yellow")
    turt.pd()
    turt.circle(80)

    turt.pu()
    turt.goto(120, -100)
    turt.color("green")
    turt.pd()
    turt.circle(80)
    turtle.done()

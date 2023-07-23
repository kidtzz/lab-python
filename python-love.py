import turtle

pen = turtle.Turtle()

def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()

def txt():
    pen.up()
    pen.setpos(-68, 95)
    pen.down()
    pen.color('lightgreen')
    pen.write('I Love You', font=("Verdana", 12, "bold"))

heart()
txt()
pen.ht()

import turtle

turtle.speed(10)
turtle.bgcolor("white")
turtle.pensize(3)

def func():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.color("red", "pink")
turtle.begin_fill()

turtle.left(140)
turtle.forward(111.65)

func()
turtle.left(120)

func()

turtle.forward(111.65)
turtle.end_fill()

turtle.hideturtle()
turtle.done()
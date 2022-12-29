from random import randint
from turtle import *
import time
import turtle

happy = turtle.Screen()

happy.bgcolor("black")

turtle = turtle.Turtle()

turtle.shape("circle")

turtle.color("yellow")

turtle.width(7)

colors = ["peru", "ivory", "dark orange", "coral", "cyan", "hot pink", "gold",
          "ivory", "yellow", "red", "pink", "green", "blue", "light blue", "light green", ]
time.sleep(5)
def draw_happy(i, x, y):

    turtle.pencolor("linen")

    turtle.color(colors[i % 7])

    turtle.begin_fill()

    turtle.lt(70)

    turtle.penup()

    turtle.goto(x, y)

    turtle.pendown()

    turtle.circle(33)

    turtle.end_fill()
def ballon(x, y):

    for i in range(5):

        draw_happy(i, x, y)
def f1():

    for i in range(7):

        turtle.pensize(5)

        turtle.pencolor('light blue')

        turtle.color(colors[i % 19])

        turtle.begin_fill()

        turtle.left(330)

        turtle.forward(55)

        turtle.begin_fill()

        turtle.rt(110)

        turtle.circle(33)

        turtle.end_fill()

        turtle.rt(11)

        turtle.backward(33)

        turtle.end_fill()


def cake(x, y):

    turtle.fd(x)

    turtle.rt(90)

    turtle.fd(y)

    turtle.rt(90)

    turtle.fd(x)

    turtle.rt(90)

    turtle.fd(y)

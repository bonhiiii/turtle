import turtle
from turtle import color
import random

def pen(colour):
    turtle.color(colour)
def fireworks(size):
    for num in range(20):
       turtle.forward(size)
       turtle.rt(180-(360/20))
turtle.bgcolor("black")
turtle.speed(0)
colors="red"
pen(colors)
fireworks(random.randint(50,100))
turtle.done()
import random
import turtle
from turtle import Turtle,Screen

kotha = Turtle()
kotha.pencolor("blue")
kotha.speed("fastest")
kotha.circle(80) #creates a circle with radius 80
turtle.colormode(255)


def random_color(): #returns a random color
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
print(kotha.heading()) #prints: 0.0 in console #Tells turtle's current heading direction


current_heading = kotha.heading()
kotha

















screen = Screen()
screen.exitonclick()
import random
import turtle
from turtle import Turtle,Screen

kotha = Turtle()
kotha.pencolor("blue")
kotha.speed("fastest")
kotha.circle(100) #creates a circle with radius 80
turtle.colormode(255)


def random_color(): #returns a random color
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
print(kotha.heading()) #prints: 0.0 in console #Tells turtle's current heading direction


def draw_spirograph(size_of_gap): #gap between each circle in DEGREES
#360 degrees in a full circle, and for each circle we are drawing we are giving it a different offset which is our size_of gap
    for _ in range(int(360 / size_of_gap)): #360 is the entire space, and if we use 5 as in input in draw_spirograph(5), then 360/5 = 72, which means 72 circles
        kotha.color(random_color())
        current_heading = kotha.heading() #gives value 0.0
        kotha.setheading(current_heading + size_of_gap) #sets the heading direction of arrow to 0.0 + 10, so shifts by 10 more degrees
        kotha.circle(100)


draw_spirograph(5)














screen = Screen()
screen.exitonclick()
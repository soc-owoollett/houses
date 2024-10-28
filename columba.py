
"""Columba generative art."""

from turtle import *
import random

# UPDATE POINTS HERE
points = 76

def grow(length, decrease, angle, noise=0):
    """Grow tree."""
    if length > 10:

        fd(length)

        new_length = length * decrease
        if noise > 0:
            new_length *= random.uniform(0.9, 1.1)

        angle_l = angle + random.gauss(0, noise)
        angle_r = angle + random.gauss(0, noise)

        left(angle_l)
        grow(new_length, decrease, angle, noise)
        right(angle_l)

        right(angle_r)
        grow(new_length, decrease, angle, noise)
        left(angle_r)

        bk(length)


def grow2(length, decrease, angle, noise=0):
    """Grow 2."""
    if length > 10:

        fd(length)

        new_length = length * decrease
        if noise > 0:
            new_length *= random.uniform(0.9, 1.1)

        angle_l = angle + random.gauss(0, noise)
        angle_r = angle + random.gauss(0, noise)

        left(angle_l)
        grow(new_length, decrease, angle, noise)
        right(angle_l)

        right(angle_r)
        grow(new_length, decrease, angle, noise)
        left(angle_r)

        bk(length)


hideturtle()
speed(0)
bgcolor("#fa3c3c")

penup()
goto(0, 250)
pendown()

pencolor("white")
write(f"Columba : {points} pts", font=("Verdana", 30, "bold"), align="center")

penup()
goto(0, -275)
pendown()

width(1.6)
left(90)
grow(100, 0.8, 20, 10)

tracer(True)
exitonclick()

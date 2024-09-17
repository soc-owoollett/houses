from turtle import *
import random

def draw_square(x,y,s):
    penup()
    goto(x-s/2,y-s/2)
    pendown()
    for i in range(4):
        fd(s)
        lt(90)

setup(500,500)
width(random.randint(0,1))
print(width)
hideturtle()
speed(0)

noise = 5
size = 100
shrink = 15


pencolor("black")
write("McRae : 470 pts", font=("Verdana", 30, "bold"), align="center")



for x in range(-500+size//2, 500, size):
    pencolor("white")
    write("McRae : 472 pts", font=("Verdana", 29, "bold"), align="center")
    write("McRae : 470 pts", font=("Verdana", 30, "bold"), align="center")
    write("McRae : 472 pts", font=("Verdana", 31, "bold"), align="center")

    pencolor("black")
    write("McRae : 470 pts", font=("Courier", 30, "bold"), align="center")
    pencolor("#4a4a4a")
    for y in range(-500+size//2, 500, size):
        draw_square(x, y, 200)

        x_off = random.uniform(-noise, noise)
        y_off = random.uniform(-noise, noise)

        for i in range(6):
            draw_square(x+i*x_off, y+i*y_off, size-i*shrink)


exitonclick()

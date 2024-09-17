import turtle as t

import random


def euler_curve(step_size, angle_step, n_steps):
    angle = 0
    for i in range(n_steps):
        t.right(angle)
        t.fd(step_size)
        angle += angle_step
        t.lt(90)


def spiral(step_size, angle_step, n_steps):
    angle = 0
    for i in range(n_steps):
        t.right(angle)
        t.fd(step_size)
        angle += angle_step


t.tracer(True)
t.bgcolor('#9bc4eb')
t.hideturtle()
t.speed(0)
t.width(1.5)

colours = ["light blue", "purple", "yellow", "orange", "pink"]

t.pencolor("blue")

t.write("Macfarlane : 701 pts", font=("Verdana", 30, "bold"), align="center")
t.penup()
t.goto(-200,200)
t.pendown()

t.pencolor("#188af5")
# Spiral 1 ----------------
euler_curve(random.randint(2,30), 2.73, random.randint(300,4000))
t.penup()
t.goto(random.randint(-700,700), random.randint(-400,400))
t.pendown()
# Spiral 2 ---------------
euler_curve(random.randint(2,30), 2.73, random.randint(300,4000))
t.penup()
t.goto(random.randint(-700,700), random.randint(-400,400))
t.pendown()
# Spiral 3 --------------
euler_curve(random.randint(2,30), 2.73, random.randint(300,4000))
euler_curve(random.randint(2,30), 2.73, random.randint(300,4000))


t.tracer(True)
t.exitonclick()

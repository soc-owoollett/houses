
"""Rutherford generative art."""

import turtle as t
import random

points = 3670

def random_color():
    """Generate a random color in hex format."""
    return f'#{random.randint(0, 0xFFFF):06x}'


def create_moving_dots(num_dots):
    """Create moving dots."""
    dots = []
    for i in range(num_dots):
        dot = t.Turtle()
        dot.shape('circle')
        dot.color(random.choice(yellows))
        dot.penup()
        dot.speed(0)
        dot.goto(random.randint(-790, 790), random.randint(-590, 590))
        dot.dx = random.randint(-50, 80)
        dot.dy = random.randint(-50, 80)
        dots.append(dot)
    return dots


def move_dots(dots):
    """Move dots continuously."""
    for dot in dots:
        dot.setx(dot.xcor() + dot.dx)
        dot.sety(dot.ycor() + dot.dy)

        # Check for collisions with the boundaries
        if dot.xcor() > 790 or dot.xcor() < -790:
            dot.dx *= -1
        if dot.ycor() > 590 or dot.ycor() < -590:
            dot.dy *= -1

    # Schedule the next update
    t.ontimer(lambda: move_dots(dots), 20)


def create_moving_art():
    """Create art and set up screen."""
    screen = t.Screen()
    screen.title("Moving Art")
    screen.bgcolor("#fff196")
    t.pencolor("#0d0c00")
    t.write(f"Rutherford : {points} pts",
            font=("Verdana", 30, "bold"), align="center")
    screen.setup(width=800, height=600)

    num_dots = 100
    dots = create_moving_dots(num_dots)

    # Schedule the first move
    move_dots(dots)

    # Keep the window open
    screen.mainloop()


yellows = ["#f7dd68", "#f5ce25", "#f7e34a", "#fce023", "#fcdf1e", "#faef25"]

# Run the program
t.hideturtle()
t.color("black")

t.shape("circle")
t.color(random.choice(yellows))

create_moving_art()

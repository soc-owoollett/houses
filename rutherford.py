import turtle as t
import random


def random_color():
    """Generate a random color in hex format."""
    return f'#{random.randint(0, 0xFFFF):06x}'


def create_moving_dots(num_dots):
    dots = []
    for i in range(num_dots):
        dot = t.Turtle()
        dot.shape('circle')
        #dot.color(random_color())
        dot.color(random.choice(yellows))
        dot.penup()
        dot.speed(0)
        dot.goto(random.randint(-790, 790), random.randint(-590, 590))
        #dot.dx = random.choice([-3, -2, -1, 1, 2, 3])
        #dot.dy = random.choice([-3, -2, -1, 1, 2, 3])
        dot.dx = random.randint(-50,80)
        dot.dy = random.randint(-50,80)
        dots.append(dot)
    return dots


def move_dots(dots):
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
    screen = t.Screen()
    screen.title("Moving Art")
    screen.bgcolor("#fff196")
    t.pencolor("#f7dc0f")
    t.write("Rutherford : 3670 pts", font=("Verdana", 30, "bold"), align="center")
    screen.setup(width=800, height=600)
    #screen.tracer(0)

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


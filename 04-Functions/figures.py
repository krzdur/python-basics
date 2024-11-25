###
# Draw a square
#
import turtle
import random


def setup_turtle(func):
    def wrapper(*args, **kwargs):
        # Set up the screen
        window = turtle.Screen()
        window.bgcolor("lightgreen")

        # Create the turtle
        pen = turtle.Turtle()
        pen.speed(5)

        func(*args, **kwargs, pen=pen)

        # Hide the turtle and finish
        pen.hideturtle()
        window.mainloop()

        return pen

    return wrapper


def draw_square(length, pen):
    # Draw a square
    for i in range(4):
        pen.forward(length)
        pen.right(90)


def draw_triangle(length, pen):
    for i in range(3):
        pen.forward(length)
        pen.left(180 - 60)


def draw_rectangle(length_a, length_b, pen):
    for i in range(2):
        pen.forward(length_a)
        pen.right(90)
        pen.forward(length_b)
        pen.right(90)


def move_pen(pen: turtle.Turtle):
    new_coordinates = (random.randint(-200, 200), random.randint(-200, 200))

    pen.penup()
    pen.goto(new_coordinates)
    pen.pendown()


@setup_turtle
def draw_figures(pen):
    for i in range(2):
        draw_square(100, pen)
        move_pen(pen)

    for i in range(2):
        draw_triangle(100, pen)
        move_pen(pen)

    for i in range(2):
        draw_rectangle(100, 50, pen)
        move_pen(pen)


if __name__ == '__main__':
    draw_figures()

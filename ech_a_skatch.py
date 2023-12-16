from turtle import Turtle
from turtle import Screen

tim = Turtle()


def move_forward():
    tim.forward(10)

def move_back():
    # heading = tim.heading()
    # tim.setheading(heading + 180)
    tim.forward(-10)

def head_right():
    tim.right(5)

def head_left():
    tim.left(5)

def clear_screen():
    tim.reset()


screen = Screen()
screen.listen()
screen.onkey(key='a', fun=head_left)
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="d", fun=head_right)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()


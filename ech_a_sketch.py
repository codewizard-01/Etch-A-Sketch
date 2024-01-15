import turtle
from turtle import Turtle
from turtle import Screen


class SketchGame:

    def __init__(self):
        self.pen = Turtle()
        self.screen = Screen()
        self.bg_colors = self.screen.textinput(title="Choose a background color!",
                                               prompt="choose: orange, grey, white.")
        if self.bg_colors == "orange":
            turtle.bgcolor("orange")
        elif self.bg_colors == "grey":
            turtle.bgcolor("lightgrey")
        elif self.bg_colors == "white":
            turtle.bgcolor("white")
        self.screen.listen()
        self.screen.onkey(key='Left', fun=self.head_left)
        self.screen.onkey(key="Up", fun=self.move_forward)
        self.screen.onkey(key="Right", fun=self.head_right)
        self.screen.onkey(key="Down", fun=self.move_back)
        self.screen.onkey(key="c", fun=self.clear_screen)
        self.screen.exitonclick()

    def move_forward(self):
        self.pen.forward(10)

    def move_back(self):
        self.pen.forward(-10)

    def head_right(self):
        self.pen.right(5)

    def head_left(self):
        self.pen.left(5)

    def clear_screen(self):
        self.pen.reset()


def start():
    SketchGame()

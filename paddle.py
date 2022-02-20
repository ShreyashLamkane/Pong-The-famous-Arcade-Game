from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.penup()
        self.speed("fastest")
        self.goto(position)
        self.color("white")
        self.resizemode("user")
        self.shapesize(stretch_len=1, stretch_wid=5)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
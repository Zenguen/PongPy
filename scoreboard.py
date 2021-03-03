from turtle import Turtle
FONT = ("Arial", 80, "normal")
ALIGN = "left"
MOVE = False


class ScoreBoard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.points = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(position)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=self.points, move=MOVE, align=ALIGN, font=FONT)

    def add_point(self):
        self.points += 1
        self.write_score()

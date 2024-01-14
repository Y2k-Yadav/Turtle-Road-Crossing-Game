from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("BLACK")
        self.setposition(0, 260)
        self.update_score()

    def update_score(self):
        self.write(f"Level = {self.level}", False, align="center", font=FONT)

    def inc_score(self):
        self.level += 1
        self.clear()
        self.update_score()



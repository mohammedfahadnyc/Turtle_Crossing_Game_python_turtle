FONT = ("Courier", 18, "normal")
SCORE_POSITION = (-270,270)
from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 0
        self.penup()
        self.goto(SCORE_POSITION)
        self.hideturtle()
        self.color("black")
        self.write(arg= f"Level is {self.score}",font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(arg= f"Level is {self.score}",font=FONT)

    def game_over(self):
        self.goto(x=0,y=0)
        self.write(arg=f"GAME OVER", font=FONT)



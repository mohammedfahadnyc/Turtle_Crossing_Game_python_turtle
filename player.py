STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.tiltangle(90)
        self.color("green")
        self.penup()
        self.goto(STARTING_POSITION)
        self.speed = MOVE_DISTANCE

    def move_up(self):
        self.sety(self.ycor()+self.speed)

    def reached_finished_line(self):
        if self.ycor() >= FINISH_LINE_Y :
            self.goto(STARTING_POSITION)
            return True

    # def level_up(self):
    #     self.speed += MOVE_DISTANCE

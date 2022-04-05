import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple","pink","teal"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.car_list = []
        self.move_speed = MOVE_INCREMENT
        self.generate_new_car()

    def move_all_cars(self):
        for car in self.car_list :
            car.goto(x=car.xcor()-self.move_speed,y=car.ycor())

    def generate_new_car(self):
        self.genetaion_pace = random.randint(1,6)
        if self.genetaion_pace == 1 :
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(x=280, y=random.randint(-240, 240))
            self.car_list.append(new_car)

    def update_car_speed(self):
        self.move_speed +=  MOVE_INCREMENT







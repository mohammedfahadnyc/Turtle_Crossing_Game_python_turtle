import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(key="Up",fun=player.move_up)
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_all_cars()
    car_manager.generate_new_car()
    if player.reached_finished_line() :
        car_manager.update_car_speed()
        scoreboard.update_score()

    for car in car_manager.car_list :
        if car.distance(player) < 20 :
            game_is_on = False
            scoreboard.game_over()




screen.exitonclick()




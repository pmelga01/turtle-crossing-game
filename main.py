import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.bgcolor("#251F47")
player = Player()
score = Scoreboard()
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.onkey(player.move, "Up")
    screen.onkey(player.move, "w")

    car_manager.create_car()
    car_manager.move_cars()
    if (player.player.ycor() > 280):
        player.reset_position()
        score.level_up()
        car_manager.level_up()
    
    for car in car_manager.all_cars:
        if (car.distance(player.player) < 20):
            score.game_over()
            game_is_on = False
            break

screen.exitonclick()


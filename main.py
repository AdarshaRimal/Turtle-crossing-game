import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("turtle-crossing")
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(player.move_turtle, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    #detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #detect turtle reaching end line

    if player.ycor() > 280:
        player.goto_start()
        car_manager.level_up()
        scoreboard.update_score()


screen.exitonclick()

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player_turtle = Player()
score = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player_turtle.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # Detect collision with a car
    for car in car_manager.all_cars:
        if car.distance(player_turtle) < 20:
            game_is_on = False
            score.game_over()


    # Checking if Turtle reaches the endpoint
    if player_turtle.is_at_finish_line():
        player_turtle.goto_start()
        score.increase_level()
        car_manager.level_up()


screen.exitonclick()

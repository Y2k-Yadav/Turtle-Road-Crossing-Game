import time
from turtle import Turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

turtle = Turtle()
screen = Screen()
screen.title("TURTLE ROAD CROSSING GAME")
car_manager = CarManager()
scoreboard = Scoreboard()
turtle.hideturtle()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(player.move, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    for car in car_manager.car_list:
        if car.distance(player) < 20:
            game_is_on = False
            turtle.color("Red")
            turtle.write("Game Over", False, align="center", font=("courier", 20, "bold"))
    if player.ycor() > 270:
        scoreboard.inc_score()
        player.starting_position()
        car_manager.level_up()



screen.exitonclick()

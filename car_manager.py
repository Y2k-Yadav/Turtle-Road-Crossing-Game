from player import Player
from turtle import Turtle
from random import randint, choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 4
MOVE_INCREMENT = 7


class CarManager:
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if randint(1,6) == 1:
            car = Turtle("square")
            car.color(choice(COLORS))
            car.setheading(180)
            car.penup()
            car.shapesize(1, 2)
            ran_y = randint(-240, 240)
            car.goto(300, ran_y)
            self.car_list.append(car)

    def move_car(self):
        for car in self.car_list:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

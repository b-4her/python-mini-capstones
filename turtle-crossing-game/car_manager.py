from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    moving_distance = STARTING_MOVE_DISTANCE

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2)
        self.penup()
        self.setheading(180)
        self.color(choice(COLORS))
        self.goto(x=310, y=randint(-250, 260))
    
    def d33s(self):
        self.forward(CarManager.moving_distance)
    
    def spead_up(self):
        CarManager.moving_distance += MOVE_INCREMENT



# ball.py
from turtle import Turtle
from random import randint

class Ball(Turtle):    

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

        x = randint(1,4)  # to get random angel without including 0 90 180 270 360
        if x == 1:
            self.angel = randint(15, 75)
        elif x == 2:
            self.angel = randint(105, 165)
        elif x == 3:
            self.angel = randint(195, 255)
        else:
            self.angel = randint(285, 345)
           
    def move(self):
        self.setheading(self.angel)
        self.forward(10)

    def bouncing_wall(self):
        self.angel = 360 - self.angel

    def bouncing_pad(self):
        self.angel = 540 - self.angel 

    def ball_reset(self, winner):
        self.teleport(x=0, y=0)
        x = randint(1, 2)
        if winner == "r_player":
            if x == 1:
                self.angel = randint(15, 75)
            else:
                self.angel = randint(285, 345)
        elif winner == "l_player":
            if x == 1:
                self.angel = randint(105, 165)
            else:
                self.angel = randint(195, 255)
            
        
        

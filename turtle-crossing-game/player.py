from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(x=STARTING_POSITION[0], y=STARTING_POSITION[1])

    def go_forward(self):
        self.forward(MOVE_DISTANCE)
    
    def go_back(self):
        if self.ycor() > FINISH_LINE_Y:
            self.teleport(x=STARTING_POSITION[0], y=STARTING_POSITION[1])
            return True
        else:
            return False
    
        


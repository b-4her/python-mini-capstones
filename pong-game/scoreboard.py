# scorebord.py
from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_player_score = 0
        self.r_player_score = 0
        self.color("white")
        self.hideturtle()
        self.pensize(3)
        self.penup()
        self.khat()
        self.score_bar()

    def khat(self):
        self.goto(x=0, y=-270)
        self.setheading(90)
        for _ in range(0, 24):
            self.pendown()
            self.forward(13)
            self.penup()
            self.forward(10)

    def score_bar(self):
        self.clear()
        self.khat()
        self.goto(x=-75, y=200)
        self.write(arg=f"{self.l_player_score}", move=False, align="center", font=("courier", 60, "normal"))       
        self.goto(x=75, y=200)
        self.write(arg=f"{self.r_player_score}", move=False, align="center", font=("courier", 60, "normal"))
        
    def add_point(self, winner):
        if winner == "r_player":
           self.r_player_score += 1
        
        else: 
           self.l_player_score += 1
        self.score_bar()
    
    def show_winner(self, winner):
        self.clear()
        self.goto(x=-75, y=200)
        self.write(arg=f"{self.l_player_score}", move=False, align="center", font=("courier", 60, "normal"))       
        self.goto(x=75, y=200)
        self.write(arg=f"{self.r_player_score}", move=False, align="center", font=("courier", 60, "normal"))
        self.goto(x=0, y=0)

        if winner == "l_player":
            self.write(arg="The left player wins!", move=False, align="center", font=("courier", 30, "normal"))
        else: 
            self.write(arg="The right player wins!", move=False, align="center", font=("courier", 30, "normal"))



        
        



   
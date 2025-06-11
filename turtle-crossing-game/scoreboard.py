from turtle import Turtle

level_FONT = ("Courier", 20, "normal")
endTitle_FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-200, y=250)
        self.player_score = 1
        self.show_score()
    
    def show_score(self):
        self.clear()
        if self.player_score == 10:
            self.write(arg=f"The last level!", move=False, align="center", font=level_FONT)
        else:
            self.write(arg=f"Level: {self.player_score}/10", move=False, align="center", font=level_FONT)
    
    def score_up(self):
        self.player_score += 1
        self.show_score()

    def end_title(self, game_statues):
        self.clear()
        if game_statues == "lose":
            self.goto(x=0, y=0)
            self.write(arg=f"   GAME OVER\nYour Score is {self.player_score}", move=False, align="center", font=endTitle_FONT)
        elif game_statues == "win":
            self.goto(x=0, y=0)
            self.write(arg=f"YOU WIN!", move=False, align="center", font=endTitle_FONT)


    

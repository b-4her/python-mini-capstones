from turtle import Turtle
import os 

os.chdir(r"C:\Users\Baher\OneDrive\Desktop\CsJourney\VScode\Projects\100 Days of Code in Python By Angela\Finished\Project_Day_20+21+24\Code")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.player_score = 0
        with open("data.txt") as data:
            self.highest_score = data.read()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.speed(0)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(arg=f"Score: {self.player_score} Highest Score: {self.highest_score}", move=False, align="center", font=("Courier", 15, "normal"))    
    
    def add_points(self):
        self.player_score += 1

    def reset(self):
        if self.player_score > int(self.highest_score):
            self.highest_score = self.player_score
            with open("data.txt", mode="w") as data:
                data.write(str(self.highest_score))
        self.player_score = 0
        self.show_score()
        
    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write(arg=f"Game Over", move=False, align="center", font=("Courier", 25, "normal"))
        
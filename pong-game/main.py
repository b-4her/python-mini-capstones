# main.py
from turtle import Turtle, Screen
from scoreboard import ScoreBoard
from pads import Paddels
from ball import Ball
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("Black")
screen.title("Pong")
screen.tracer(0)

l_pad = Paddels(ycor=0, xcor=-350)
r_pad = Paddels(ycor=0, xcor=350)

screen.listen()
screen.onkeypress(r_pad.go_up, "Up") 
screen.onkeypress(r_pad.go_down, "Down") 
screen.onkeypress(l_pad.go_up, "w") 
screen.onkeypress(l_pad.go_down, "s") 
# Higher order functions

score = ScoreBoard()

ball = Ball()

x = 0.08
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(x)

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bouncing_wall()
        while ball.ycor() > 290 or ball.ycor() < -290:
            ball.move() 

    # if ball.distance(r_pad) < 30 or ball.distance(l_pad) < 30: #old code for bouncing 
    #     ball.bouncing_pad()
    #     if x > 0.02:
    #          x -= 0.02 
    #     time.sleep(x)
    #     while ball.distance(r_pad) < 30 or ball.distance(l_pad) < 30:
    #         ball.move()
        
    if ball.distance(r_pad) < 50 and ball.xcor() > 320: 
        ball.bouncing_pad()
        if x > 0.02:
             x -= 0.02 
        time.sleep(x)
        while ball.distance(r_pad) < 50 and ball.xcor() > 320:
            ball.move()

    if ball.distance(l_pad) < 50 and ball.xcor() < -320:
        ball.bouncing_pad()
        if x > 0.02:
             x -= 0.02 
        time.sleep(x)
        while ball.distance(l_pad) < 50 and ball.xcor() < -320:
            ball.move()
    
    ball.move()
    
    if ball.xcor() > 390:
        ball.ball_reset("l_player") 
        score.add_point("l_player")
        x = 0.08
        if score.l_player_score == 5:
            game_is_on = False
            score.show_winner("l_player")

    elif ball.xcor() < -390:
        ball.ball_reset("r_player")
        score.add_point("r_player")
        x = 0.08
        if score.r_player_score == 5:
            game_is_on = False
            score.show_winner("r_player")



screen.exitonclick()
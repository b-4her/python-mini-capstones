import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("The Turtle Crossing")

player = Player()
score = Scoreboard()
score.show_score()

screen.listen()
screen.onkeypress(player.go_forward, "Up")


my_cars = []
n = 0 # to make the car generate every one second (0.1*10 = 1)
x = 14
game_is_on = True
while game_is_on:  
    time.sleep(0.1)
    screen.update()
    
    if n % x == 0:
        for add_car in range(0,2):
            new_car = CarManager()
            my_cars.append(new_car)

    for car in my_cars:
        car.d33s()

    if player.go_back():
        for car in my_cars :
            car.teleport(x=320, y=0)
        x -= 1
        car.spead_up() 
        score.score_up()
        player.go_back()
        
    for car in my_cars:
        if player.distance(car) < 25:
            game_is_on = False
            score.end_title("lose")
        
    if score.player_score == 10 :
        game_is_on = False
        score.end_title("win")
    n += 1

screen.exitonclick()
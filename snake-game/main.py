from turtle import Screen, Turtle
from scoreboard import Score
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up") 
screen.onkey(snake.down, "Down") 
screen.onkey(snake.right, "Right") 
screen.onkey(snake.left, "Left") 
#Higher order function
 
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.add_points()
        score.show_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_on = False
        # score.game_over()
            # score.show_score()
            score.reset()
            snake.reset_cordination()

    for part in snake.my_snake[1:]:    
        if snake.head.distance(part) < 10: # and part != snake.head # you can use this too instead of using slicing lists 
            # game_is_on = False
            # score.game_over() 
            # score.show_score()
            score.reset()
            snake.reset_cordination()  
            screen.update()       

screen.exitonclick()
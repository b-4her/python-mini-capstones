from turtle import Turtle

STARTING_CORDINATES = [(0,0) , (-20,0), (-40,0)]
MOVE_DISTANCE = 20
Current_Heading = 180
UP = 90
DOWN = 270 
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self): 

        self.my_snake = []
        self.creat_snake()
        self.extend_times = 0
        self.head = self.my_snake[0]
    
    def creat_snake(self):
        for position in STARTING_CORDINATES:
            snake_part = Turtle("square")
            snake_part.color("white")
            snake_part.penup()
            snake_part.goto(position)
            self.my_snake.append(snake_part)
        
    def extend(self):
        self.extend_times += 1
        snake_part = Turtle("square")
        snake_part.color("white")
        snake_part.penup()
        
        new_x = self.my_snake[-1].xcor()        
        new_y = self.my_snake[-1].ycor() 

        snake_part.goto(new_x, new_y)
        self.my_snake.append(snake_part)
        

    def move(self):
        for part in range(len(self.my_snake) - 1, 0, -1):
            new_x = self.my_snake[part - 1].xcor()       
            new_y = self.my_snake[part - 1].ycor() 
            self.my_snake[part].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
           self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
           self.head.setheading(DOWN)      

    def right(self):
        if self.head.heading() != LEFT:
           self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
           self.head.setheading(LEFT)

    def reset_cordination(self):
        for part in self.my_snake:
            part.hideturtle()
        self.my_snake.clear()
        self.creat_snake()
        self.head = self.my_snake[0]


        # old_snake = self.my_snake
        # for times in range(-1, -self.extend_times-1, -1):
        #     removed_pice = old_snake[times]
        #     self.my_snake.remove(removed_pice)
        #     removed_pice.hideturtle()
        # self.extend_times = 0
        # self.head.teleport(x=0, y=0)

        

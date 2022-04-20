import time
from turtle import Turtle

#global CONST (starting position of snake body)
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0
MOVE_DISTANCE = 20
#DEFINE snake class
class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        # for loop that create a basic snake_body
        for i in STARTING_POSITIONS:
            snake_body_fragment = Turtle()
            snake_body_fragment.penup()
            snake_body_fragment.color("white")
            snake_body_fragment.shape("square")
            snake_body_fragment.goto(i)
            self.snake_body.append(snake_body_fragment)  # Create segments of snake body



    def snake_move(self):
        # moving fragment's of the snake body
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[seg_num].goto(self.snake_body[seg_num - 1].xcor(), self.snake_body[seg_num - 1].ycor())
        self.snake_body[0].forward(MOVE_DISTANCE)

        #turn left or right functions
    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

        #adding new segment to snake
    def add_new_segment(self):
        snake_body_fragment = Turtle()
        snake_body_fragment.penup()
        snake_body_fragment.color("white")
        snake_body_fragment.shape("square")
        self.snake_body.append(snake_body_fragment)

    def sub_new_segment(self):
        #$self.snake_body[len(self.snake_body)].goto(1000,1000)
        self.x=self.snake_body.pop()
        self.x.goto(1000,1000)

        #send old snake_body out of screen and design new snake_body
    def reset(self):
        for seg in self.snake_body:
            seg.goto(1000,1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]


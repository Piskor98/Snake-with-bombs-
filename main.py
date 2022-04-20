#import basic libraries
from snake import Snake
import time
from turtle import Turtle,Screen
from food import Food
from scoreboard import scoreboard
import playsound
import winsound
from Bomb import Bomb
# from Speed_objects import speed
# Basic properties of screen
screen = Screen()                   #create a screen object
screen.setup(600,600)               #setup screen
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0,0)                  #turn off the tracer
screen.listen()                     #interaction with gui

#Create snake object
snake = Snake()
food = Food()
is_snake_alive = True
bomb = Bomb()
# Turn left or right the snake body
screen.listen()
screen.onkey(key="a", fun=snake.move_left)
screen.onkey(key="w", fun=snake.move_up)
screen.onkey(key="s", fun=snake.move_down)
screen.onkey(key="d", fun=snake.move_right)
# speed_object=speed()
#create scoreboard
scoreboard = scoreboard()
t=0.05
# snake move
while is_snake_alive:
    # speed_object.create_object_speed()
    snake.snake_move()
    screen.update()
    time.sleep(t)

    # detect the collision with food
    if snake.head.distance(food)<20:
        winsound.PlaySound("./nom.wav", winsound.SND_ASYNC)
        snake.add_new_segment()
        food.refresh()
        bomb.refresh()
        scoreboard.increase_score()

    #detect the collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() >290 or snake.head.ycor() <-290:
        snake.reset()
        scoreboard.reset()
        winsound.PlaySound("./losing.wav", winsound.SND_ASYNC)


    if snake.head.distance(bomb)<20:
        snake.sub_new_segment()
        bomb.refresh()
        scoreboard.decrease_score()
#ASYNCHORNIZACJA - BRAK
    # if snake.head.distance(speed)<20:
    #     t-=0.01
    #     speed_object.refreash()


    # if snake.head.xcor()  ==  snake.snake_body[i].xcor()

    #Detect collision with tail
    #if head collides with any segment in the tail:
        #trigger game_over
    for segment in snake.snake_body[1:]:
        # if segment ==snake.head:
        #     pass
        if snake.head.distance(segment)<10:
            winsound.PlaySound("./losing.wav", winsound.SND_ASYNC)
            scoreboard.reset()
            snake.reset()



# Exit game




screen.exitonclick()

### Slicing

# number_list = [1,2,3,4,5,6,7,8,9,0]
#
# print(number_list[3:5])             #4,5
# print(number_list[2:8:3])           #3,6
# print(number_list[:5])
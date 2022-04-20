
from turtle import Turtle
import random

class Bomb(Turtle):
    def __init__(self):
        super(Bomb, self).__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.goto(random.randint(-280,280),random.randint(-280,280))




    def refresh(self):
        self.goto(random.randint(-280, 280), (random.randint(-280, 280)))


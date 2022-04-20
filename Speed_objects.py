# import time
# from turtle import Turtle
# import random
#
# class speed:
#     def __init__(self):
#         self.objects =[]
#         self.t=30
#         self.create_object_speed()
#
#
#     def create_object_speed(self):
#         while self.t > 0:
#             time.sleep(1)
#             self.t -= 1
#         if self.t ==0:
#             self.speed = Turtle()
#             self.speed.penup()
#             self.speed.color('green')
#             self.speed.shape('triangle')
#             self.speed.goto(random.randint(-280,280),random.randint(-280,280))
#             self.objects.append(self.speed)
#             self.t=30
#
#     def refreash(self):
#         for i in  self.objects:
#             i.goto(random.randint(-280,280),random.randint(-280,280))
#


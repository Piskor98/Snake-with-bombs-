
from turtle import Turtle

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open ("scoreboard.txt") as file:
            self.highscore = int(file.read())

        self.hideturtle()
        self.goto(0, 270)
        self.color('White')
        self.write(f'Score: {self.score} High Score: {self.highscore}', align='center', font=('Arial', 16, 'normal'))

    def update_scoreboard(self):

        self.clear()
        self.write(f'Score: {self.score} High Score: {self.highscore}', align='center', font=('Arial', 16, 'normal'))

    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("scoreboard.txt", mode="w") as file:
                file.write(f"{self.highscore}")

        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score +=1
        self.update_scoreboard()

    def decrease_score(self):
        self.score -= 1
        self.update_scoreboard()


    # def game_over(self):
    #
    #     self.goto(0,0)
    #     self.write(f'Game Over', align='center', font=('Arial', 16, 'normal'))
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(-70,260)
        self.write("Score: " + str(self.score), font=("Arial", 24, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",align="Center", font=("Arial", 24, "bold"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.write("Score: " + str(self.score), font=("Arial", 24, "bold"))

        
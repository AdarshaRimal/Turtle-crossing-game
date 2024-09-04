from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.goto(0,250)
        self.update_score()



    def update_score(self):
        self.clear()
        self.write(f"Level : {self.score}", align="center", font=FONT)
        self.score += 1

    def game_over(self):
        self.color("red")
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)



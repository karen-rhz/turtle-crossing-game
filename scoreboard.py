from turtle import Turtle, Screen
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        # So it doesn't overwrite the previous score
        self.clear()
        self.goto(-250, 250)
        self.write(arg=f"Level: {self.score}", font=FONT)

    def plus_one_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        # Game over display
        self.hideturtle()
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)
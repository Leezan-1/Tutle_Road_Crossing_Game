from turtle import Turtle


FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        
        self.level = 1
        self.level_speed = 0.1
        
        # SCOREBAORD SETUP
        
        self.color('black')
        self.hideturtle()
        self.penup()
        self.goto(-275,250)  
        self.update()
 
    
    def update(self):               # score board update
        self.clear()
        self.write(f"Level: {self.level}",font=FONT)
    
    def next_level(self):           # next level increment

        self.level += 1
        self.update()
        self.level_speed *= 0.7     # speed of each level
    
    def game_over(self):            # game over prompt
        self.goto(0,0)
        self.write("Game Over!",align='center', font=FONT)

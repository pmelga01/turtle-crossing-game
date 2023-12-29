from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
        self.player = Turtle()
        self.player.shape("turtle")
        self.player.color("#b2c9ab")
        self.player.penup()
        self.player.setheading(90) #face upwards
        self.player.goto(STARTING_POSITION)

    def move(self):
        self.player.forward(MOVE_DISTANCE)
    
    def reset_position(self):
        self.player.goto(STARTING_POSITION)

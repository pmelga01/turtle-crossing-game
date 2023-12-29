import random
from turtle import Turtle

COLORS = ["#F4A5AE", "#AA7DCE", "#A8577E", "#0075f2", "#FFA737", "#7C3626"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1



class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.frequency = 20 # 1 in 20 chance of a car being made
    
    def create_car(self):
        random_chance = random.randint(1, self.frequency) # 1 in 6 chance of a car being made
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.setheading(180) #face left
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250)) #random starting height
            self.all_cars.append(new_car)
    
    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

            if (car.xcor() < -320): #infinite cars would be bad
                self.all_cars.remove(car)
    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        if (self.frequency > 3):
            self.frequency -= 1
        

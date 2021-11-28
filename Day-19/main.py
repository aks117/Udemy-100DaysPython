import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race?\n Enter a color : ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

is_race_on = False

y_pos = -150
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos)
    all_turtles.append(new_turtle)
    y_pos += 50

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner.")
            else:
                print(f"You've lost. The {winning_color} is the winner.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



# # Etch-a-Sketch
#
# def move_forward():
#     tim.forward(10)
#
#
# def move_backward():
#     tim.backward(10)
#
#
# def turn_right():
#     angle = tim.heading()
#     tim.setheading(angle-20)
#     tim.forward(10)
#
#
# def turn_left():
#     angle = tim.heading()
#     tim.setheading(angle+20)
#     tim.forward(10)
#
#
# def screen_clear():
#     tim.clear()
#     tim.reset()
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="c", fun=screen_clear)

screen.setup(width=500, height=400)





screen.exitonclick()

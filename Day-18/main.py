from turtle import Turtle, Screen
from random import randint, choice

screen = Screen()
timo = Turtle()
timo.shape("turtle")
timo.color("green")

# # Draw a square
# for _ in range (4):
#     timo.forward(100)
#     timo.right(90)

# # Drawing a dashed line
# for _ in range (20):
#     timo.forward(10)
#     timo.penup()
#     timo.forward(10)
#     timo.pendown()

# # Drawing different shapes with Turtle
# for i in range(3, 11):
#     screen.colormode(255)
#     timo.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
#     angle = 360 / i
#     k = i
#     while k > 0:
#         timo.forward(100)
#         timo.right(angle)
#         k -= 1

# # Draw a random walk
# directions = [0, 90, 180, 270]
# timo.pensize(15)
#
# for _ in range(200):
#     screen.colormode(255)
#     timo.color(randint(0, 255), randint(0, 255), randint(0, 255))
#     timo.speed(randint(2, 8))
#     timo.forward(50)
#     timo.setheading(choice(directions))

# # Drawing a spirograph
# angle = 0
# timo.speed("fastest")
# while angle <= 360:
#     screen.colormode(255)
#     timo.color(randint(0, 255), randint(0, 255), randint(0, 255))
#     angle += 5
#     timo.circle(100)
#     timo.left(angle)


screen.exitonclick()
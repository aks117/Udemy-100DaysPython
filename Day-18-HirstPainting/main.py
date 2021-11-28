# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

from turtle import Turtle as T, Screen
import random as R


screen = Screen()
screen.colormode(255)
turtle = T()

color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

turtle.penup()
turtle.hideturtle()
turtle.speed("fastest")
turtle.setheading(255)
turtle.fd(300)
turtle.setheading(0)

for i in range(10):
    for _ in range(10):
        turtle.dot(15, R.choice(color_list))
        turtle.fd(50)
    if i % 2 == 0:
        turtle.left(90)
        turtle.fd(50)
        turtle.left(90)
        turtle.fd(50)
    else:
        turtle.right(90)
        turtle.fd(50)
        turtle.right(90)
        turtle.fd(50)

screen.exitonclick()

# import colorgram
#
# Extract 30 colors from an image.
# colors = colorgram.extract('image.jpg', 30)
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
#
# print(rgb_colors)

import turtle as t
import random

color_list = [
    (8, 16, 67),
    (63, 8, 28),
    (192, 70, 22),
    (144, 11, 35),
    (248, 237, 242),
    (13, 45, 142),
    (30, 103, 175),
    (123, 162, 201),
    (249, 216, 64),
    (170, 16, 5),
    (204, 71, 124),
    (62, 34, 12),
    (224, 135, 86),
    (12, 45, 32),
    (200, 174, 38),
    (143, 194, 173),
    (213, 74, 55),
    (174, 50, 76),
    (59, 161, 118),
    (252, 206, 0),
    (215, 134, 145),
    (78, 111, 80),
    (82, 111, 199),
    (12, 100, 4),
    (177, 185, 218),
    (231, 166, 180),
    (237, 171, 160)
]

tim = t.Turtle()
tim.hideturtle()
tim.speed(0)
t.colormode(255)
tim.penup()

pos_x = -250
pos_y = -250
for pos in range(10):
    tim.setpos(pos_x, pos_y)
    for dot in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    pos_y += 50

screen = t.Screen()
screen.exitonclick()

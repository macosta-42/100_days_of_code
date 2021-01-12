import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
# tim.shape("turtle")
# tim.color("DarkSeaGreen")
#
# tim.forward(100)
# tim.right(90)
#
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
#
# for _ in range(15):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#
#
# def change_color():
#     R = random.random()
#     B = random.random()
#     G = random.random()
#     tim.color(R, G, B)
#
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     change_color()
#     draw_shape(shape_side_n)


# def change_color():
#     R = random.random()
#     B = random.random()
#     G = random.random()
#     tim.color(R, G, B)
#
#
# def random_movement():
#     number = random.randint(0, 1)
#     change_color()
#     if number == 0:
#         tim.right(90)
#         number = random.randint(0, 1)
#         if number == 0:
#             tim.forward(50)
#         else:
#             tim.backward(50)
#     else:
#         tim.left(90)
#         number = random.randint(0, 1)
#         if number == 0:
#             tim.forward(50)
#         else:
#             tim.backward(50)
#
#
# tim.pensize(10)
# for _ in range(0, 101):
#     random_movement()


# def change_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     tim.color(r, g, b)
#
#
# directions = [0, 90, 180, 270]
# tim.width(15)
# tim.speed(0)
#
# for _ in range(200):
#     change_color()
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.color(r, g, b)


def draw_circle(radius):
    tim.circle(100)
    tim.setheading(radius)


tim.speed(0)
angle = 0
in_between = 5
limit = 360 // in_between
for _ in range(limit):
    angle += in_between
    change_color()
    draw_circle(angle)

screen = t.Screen()
screen.exitonclick()

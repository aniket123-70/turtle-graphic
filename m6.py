import random
import turtle as turtle_module

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(251, 250, 247), (240, 241, 244), (230, 215, 101), ( 234, 246, 242), (154, 80, 38), (244, 231, 236), (207, 159, 105), (181, 175, 18), (108, 165, 210), (25, 91, 160), (106, 176, 124), (194, 91, 105), (13, 37, 97), (72, 43, 23), (50, 121, 23), (187, 133, 150), (94, 192, 47), (106, 32, 54), (195, 94, 75), (25, 97, 25), (100, 120, 169), (180, 206, 170), (250, 169, 173), ( 24, 53, 110), (251, 171, 163), (149, 191, 244), (104, 60, 18), (81, 30, 46), (132, 79,  90), (18,  75,  105)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
       tim.setheading(98)
       tim.forward(58)
       tim.setheading(180)
       tim.forward(500)
       tim.setheading(0)






screen = turtle_module.Screen()
screen.exitonclick()
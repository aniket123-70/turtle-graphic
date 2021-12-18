import turtle as t
import random
tim = t.Turtle()
t.colormode(225)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.speed("fastest")

def darw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color("green", "red")
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)
        tim.circle(100)

darw_spirograph(5)



screen = t.Screen()
screen.exitonclick()
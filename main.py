# Python program to draw
# Rainbow Benzene
# using Turtle Programming
import turtle


colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow','indigo']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(180):
    t.pencolor(colors[x%7])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)
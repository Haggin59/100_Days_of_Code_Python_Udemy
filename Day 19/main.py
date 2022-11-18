from turtle import Turtle,Screen

#hp kittila

scr = Screen()
scr.setup(width=500, height=400)

user_input = scr.textinput("Input", "Enter your bet (color):")
colors = ['red', 'orange', 'green', 'yellow', 'blue', 'purple']

turtles = []
x = -230
y = 100


for i in range(5):
    turtles.append(Turtle())
    turtles[i].shape("turtle")
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(x,y)
    y -= 50


 




scr.exitonclick()
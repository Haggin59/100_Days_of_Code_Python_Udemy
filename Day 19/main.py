#turtle race

from turtle import Turtle,Screen
import random

#hp kittila

scr = Screen()
scr.setup(width=500, height=400)

user_input = scr.textinput("Input", "Enter your bet (color):")
colors = ['red', 'orange', 'green', 'yellow', 'blue']

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

run = True

while run:

    for i in range(5):

        turtles[i].forward(random.randint(10,30))
        
        p = turtles[i].position()
        if p[0] >= 250:
            run = False
            break

print("user_input",user_input)
print("Winner:", i)

if user_input == str(i):
    print("You Win")

else:
    print("You loose")
 




scr.exitonclick()
from turtle import Turtle,Screen
import random

t1 = Turtle()
t1.shape('arrow')
t1.color('tomato')

screen = Screen()
screen.bgcolor('black')
screen.title("My turtle")
screen.colormode(255)


###### Side Quest######
# dist = 0
# while True:

#     dist += 10
#     t1.forward(dist)
#     t1.right(90)
#     t1.forward(dist)
#     t1.right(90)
#######################


#Challenge 1: Draw a square #######

# for i in range(4):
#     t1.forward(100)
#     t1.right(90)

#######################################



#Challenge 2: Dashed line ##########

# for i in range(50):
#     t1.pendown()
#     t1.forward(10)
#     t1.penup()
#     t1.forward(10)

#######################################

#Challenge 3: Drawing different shapes

# sides = 3

# for i in range(8):

#     for i in range(sides):
#         angle_sum = (sides-2)*180
#         ang = angle_sum/sides

#         t1.forward(100)
#         t1.right(180 - ang)
    
#     sides += 1

#########################################

#Challenge 4: Random walk ###############


# dir = [90,180,270,360]

# t1.pensize(5)

# while True:

#     t1.right(random.choice(dir))
#     t1.pencolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
#     t1.forward(20)


##########################################

#Challenge 5: Drawing a spirograph:

while True:

    t1.circle(100)
    t1.right(10)
    t1.pencolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

    




   





screen.exitonclick()
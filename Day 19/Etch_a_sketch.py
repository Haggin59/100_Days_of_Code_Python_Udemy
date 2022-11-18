#Etch a sketch

from turtle import Turtle,Screen

t1 = Turtle()
scr = Screen()

def move_fd():
    t1.forward(10)

def move_bk():
    t1.backward(10)

def turn_r():
    t1.right(10)

def turn_l():
    t1.left(10)

def clrscr():
    t1.reset()


scr.listen()
scr.onkey(fun = move_fd, key = "w") #Higher order functions
scr.onkey(fun = move_bk, key = "s")
scr.onkey(fun = turn_l, key = "a")
scr.onkey(fun = turn_r, key = "d")
scr.onkey(fun = clrscr, key = "c")








scr.exitonclick()
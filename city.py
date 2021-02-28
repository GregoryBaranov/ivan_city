from turtle import *
speed(1000)
def skai():
    begin_fill()
    color('purple')
    goto(-250,0)
    forward(500)
    left(90)
    forward(250)
    left(90)
    forward(500)
    left(90)
    forward(250)
    end_fill()

def lend():
    color('green')
    penup()
    goto(-250,0)
    begin_fill()
    pendown()
    forward(250)
    left(90)
    forward(500)
    left(90)
    forward(250)
    left(90)
    forward(500)
    end_fill()

def home():
    begin_fill()
    color('grey')
    penup()
    goto(-230,-100)
    pendown()
    left(90)
    left(90)
    forward(200)
    left(90)
    forward(250)
    left(90)
    forward(200)
    left(90)
    forward(250)
    end_fill()
def sun():
    color('red')
    penup()
    goto(210,100)
    begin_fill()
    circle(50)
    end_fill()

def window():
    begin_fill()
    for i in range(4):
        forward(50)
        left(90)
    end_fill()

def windows():
    color('yellow')
    penup()
    goto(-210,120)
    pendown()
    window()
    penup()
    goto(-100,120)
    pendown()
    window()
    penup()
    goto(-210,0)
    pendown()
    window()
    penup()
    goto(-100,0)
    pendown()
    window()

# def door():
    
def start():
    skai()
    lend()
    home()
    sun()
    windows()
   

start()
exitonclick()

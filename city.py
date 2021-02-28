from turtle import *
from random import randint
from time import sleep
w = 150
h = 150

t1 = Turtle()
t1.color('blue')
t1.width(5)
t1.shape('turtle')

t2 = Turtle()
t2.color('red')
t2.width(5)
t2.shape('turtle')
t2.left(120)

t3 = Turtle()
t3.color('green')
t3.width(5)
t3.shape('turtle')
t3.right(120)

def catch1(x,y):
    t1.penup()
    t1.goto(randint(-w,w), randint(-h,h))
    t1.pendown()
    t1.left(randint(0,180))

def catch2(x,y):
    t2.penup()
    t2.goto(randint(-w,w), randint(-h,h))
    t2.pendown()
    t2.left(randint(0,180))

def catch3(x,y):
    t3.penup()
    t3.goto(randint(-w,w), randint(-h,h))
    t3.pendown()
    t3.left(randint(0,180))


t1.onclick(catch1)
t2.onclick(catch2)
t3.onclick(catch3)

def gameFinished(t1, t2, t3):
  t1_outside = abs(t1.xcor()) > w or abs(t1.ycor()) > h
  t2_outside = abs(t2.xcor()) > w or abs(t2.ycor()) > h
  t3_outside = abs(t3.xcor()) > w or abs(t3.ycor()) > h
  isOutside = t1_outside or t2_outside or t3_outside
  return isOutside


while gameFinished(t1,t2,t3) != True:
   t1.forward(7)
   t2.forward(7)
   t3.forward(7)
   sleep(0.1)

exitonclick()

#Space Invaders

import turtle
import os

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("The Game")

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)

player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 15

#player left
def move_left():
    x = player.xcor()
    x -= playerspeed
    player.setx(x)

#player right
def move_right():
    x = player.xcor()
    x += playerspeed
    player.setx(x)

turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")




delay = input("Wait")
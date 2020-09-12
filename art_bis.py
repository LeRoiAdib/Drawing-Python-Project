"""
This file is written by Romain
"""

from turtle import Screen, Turtle
from random import randint
from random import choice
from string import ascii_letters
from sys import argv

screen = Screen()
turtle = Turtle()


def drawArt(nbOfTurns:int):
    turn = nbOfTurns
    turtle.penup()
        #caractere aléatoire
    coin_flip = randint(0,3)  
        #pour commander la tortue
    turtle.speed(100)
    if coin_flip == 0:
        drawSquare(nbOfTurns)
        turn -= 1

    elif coin_flip == 1:
        drawCircle(nbOfTurns)  
        turn -= 1
    
    elif coin_flip == 2:
        drawTriangle(nbOfTurns)
        turn -= 1
    
    elif coin_flip == 3:
        drawLetter(nbOfTurns)
        turn -= 1

def drawSquare(nbOfTurns):
    pen_size = randint(1, 5)
    size = randint(25,250)
    if size >= 25 and size < 50:
        position_x = randint(-960, 960)
        position_y = randint(-130, 80)
    elif size <= 250 and size > 50:
        position_x = randint(-960, 960)
        position_y = randint(-160,160)
    rgb_r = randint(0,255)
    rgb_g = randint(0,255)
    rgb_b = randint(0,255)
    turtle.pensize(pen_size)
    turtle.color(int(rgb_r),int(rgb_g),int(rgb_b))
    turtle.setheading(0)
    turtle.goto(position_x,position_y)
    turtle.pendown()
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.penup()
    drawArt(nbOfTurns)

def drawCircle(nbOfTurns):
    pen_size = randint(1, 5)
    size = randint(25,250)
    if size >= 25 and size < 50:
        position_x = randint(-960, 960)
        position_y = randint(-130, 80)
    elif size <= 250 and size > 50:
        position_x = randint(-960, 960)
        position_y = randint(-160,160)
    rgb_r = randint(0,255)
    rgb_g = randint(0,255)
    rgb_b = randint(0,255)
    turtle.pensize(pen_size)
    turtle.color(int(rgb_r),int(rgb_g),int(rgb_b))
    turtle.setheading(0)
    turtle.goto(position_x,position_y)
    turtle.pendown()
    turtle.circle(size)
    turtle.penup()
    drawArt(nbOfTurns)

def drawTriangle(nbOfTurns):
    pen_size = randint(1, 5)
    size = randint(25,250)
    if size >= 25 and size < 50:
        position_x = randint(-960, 960)
        position_y = randint(-130, 80)
    elif size <= 250 and size > 50:
        position_x = randint(-960, 960)
        position_y = randint(-160,160)
    rgb_r = randint(0,255)
    rgb_g = randint(0,255)
    rgb_b = randint(0,255)
    turtle.pensize(pen_size)
    turtle.color(int(rgb_r),int(rgb_g),int(rgb_b))
    turtle.setheading(0)
    turtle.goto(position_x,position_y)
    turtle.pendown()
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.penup()
    drawArt(nbOfTurns)

def drawLetter(nbOfTurns):
    letter = choice(ascii_letters)
    pen_size = randint(1, 5)
    size = randint(25,250)
    if size >= 25 and size < 50:
        position_x = randint(-960, 960)
        position_y = randint(-130, 80)
    elif size <= 250 and size > 50:
        position_x = randint(-960, 960)
        position_y = randint(-160,160)
    rgb_r = randint(0,255)
    rgb_g = randint(0,255)
    rgb_b = randint(0,255)
    turtle.pensize(pen_size)
    turtle.color(int(rgb_r),int(rgb_g),int(rgb_b))
    turtle.setheading(0)
    turtle.goto(position_x,position_y)
    turtle.pendown()
    turtle.write(letter)
    turtle.penup()
    drawArt(nbOfTurns)

screen.mainloop()

if __name__ == "__main__":
    drawArt(argv[0])
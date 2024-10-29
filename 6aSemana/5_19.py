import turtle
from random import randint
import math

def grelha(t: turtle.Turtle, l,w, cd):

    t.setheading(0)
    pos = t.pos()

    if l % cd != 0 or w % cd != 0:
        raise ValueError("Tamanho da grelha tem que ser proporcional")
    
    for i in range(2):
        t.fd(w)
        t.lt(90)
        t.fd(l)
        t.lt(90)

    cur_direction = -1
    for i in range( w // cd):
        t.fd(cd)
        cur_direction *= -1
        t.goto(t.xcor(), t.ycor() + l * cur_direction)
      
    t.lt(90)

    t.penup()
    t.setpos(pos)
    t.pendown()
    cur_direction = -1 

    for i in range(1, l // cd):
        t.fd(cd)
        cur_direction *= -1 
        t.goto(t.xcor() + w * cur_direction, t.ycor())


def game(t: turtle.Turtle, tiles, cell):

    # Adjust the initial point for better display in screen
    h = tiles*cell // 2
    t.teleport(-h, -h)

    # left down corner
    ini_x, ini_y = t.pos()
    # upper right
    ur_x , ur_y = ini_x + (cell * tiles), ini_y + (cell * tiles)
    t.color("light gray")
    grelha(t, tiles*cell, tiles*cell ,cell)

    start_x = ini_x + randint(0, tiles) * cell
    start_y = ini_y + randint(0, tiles) * cell

    print("ini coord", start_x, start_y)

    end_x = ini_x + randint(0, tiles) * cell
    end_y = ini_y + randint(0, tiles) * cell

    print("end coord", end_x, end_y)

    t.teleport(end_x, end_y)
    sh = t.shapesize()
    t.color("green")
    t.shape("square")
    t.shapesize(0.3,0.3)
    t.stamp()


    t.shapesize(0.5,0.5)
    t.shape("triangle")

    t.teleport(start_x, start_y)
    t.color("red")
    t.dot(5)


    print("Starting random walkin")
    steps = 0

    # Using round since the position is a float with high precision
    y = round(t.ycor())
    x = round(t.xcor())
    while not (x == end_x and y == end_y):
        print("teste: ", x,end_x, y,end_y)
        # 0 = up
        # 1 = right
        # 2 = left
        # 3 = down
        m = randint(0,3)

        if m == 0 and y < ur_y:  # UP
            t.setheading(90)
        elif m == 1 and x < ur_x:  # RIGHT
            t.setheading(0)
        elif m == 2 and x > ini_x: # LEFT
            t.setheading(180)
        elif m == 3 and y > ini_y: # DOWN
            t.setheading(270)
        else:
            print("Forbidden movement: ",m, x, y)
            continue

        t.fd(cell)
        y = round(t.ycor())
        x = round(t.xcor())
        steps+=1

    t.color("green")
    t.stamp()
    
    print("Reached the goal with ", steps, "steps!")


t = turtle.Turtle()
game(t, 5,40)

turtle.exitonclick()
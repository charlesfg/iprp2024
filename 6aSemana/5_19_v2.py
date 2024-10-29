import turtle
import math
import random
import time





def square(t, cell, x, y):
    t.teleport(x, y)
    for i in range(4):
        t.fd(cell)
        t.lt(90)

def grelha(t, dim, cell):

    inipos = t.pos()
    for i in range(dim):
        for j in range(dim):
            square(t, cell, inipos[0]+(i*cell), inipos[1]+(j*cell))



def game(t, dim, cell):

    
    t.teleport(-(dim*cell//2), -(dim*cell//2))

    # initial position, relative referential 0,0
    lim_lb = t.pos()
    lim_ru = (dim * cell + lim_lb[0]), dim * cell + lim_lb[1]

    # draw board
    grelha(t, dim, cell)

    # choose a random start
    start_x = random.randint(0, dim) * cell + lim_lb[0]
    start_y = random.randint(0, dim) * cell + lim_lb[1]

    # choose a random target end
    end_x = random.randint(0, dim) * cell + lim_lb[0]
    end_y = random.randint(0, dim) * cell + lim_lb[1]


    t.teleport( end_x, end_y)
    t.color("green")
    t.shape("square")
    t.shapesize(0.3,0.3)
    t.stamp()

    t.shapesize(0.5,0.5)
    t.shape("triangle")

    
    t.teleport(start_x, start_y)
    t.color("red")
    t.dot(5)

    x = start_x
    y = start_y

    s = 0

    while not (x == end_x and y == end_y):

        # Movement ...
        m = random.choice(['N','S','L','O'])
        #print(f"Moving {m} ...")

        if m == 'N' and y < lim_ru[1]:
            t.setheading(90)
            t.fd(cell)
            y+=cell
        elif m == 'S' and y > lim_lb[1]:
            t.setheading(270)
            t.fd(cell)
            y-=cell
        elif m == 'L' and x < lim_ru[0]:
            t.setheading(0)
            t.fd(cell)
            x+=cell
        elif m == 'O' and x > lim_lb[0]:
            t.setheading(180)
            t.fd(cell)
            x-=cell
        else:
            #print(f"Forbidden movement ({m}): ",x, y, end_x, end_y)
            continue
        s+=1
    
    print(f"Ended for dimension {dim}  steps {s}!")
    
    pass


t = turtle.Turtle()
turtle.delay(1)
#turtle.tracer(1,1)


for i in range(1, 10):
    t.teleport(0,0)
    t.color("light gray")
    game(t, i, 20)
    time.sleep(2)
    
    t.clear()

turtle.exitonclick()
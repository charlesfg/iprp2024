import turtle


def arc(t: turtle.Turtle, r=100, ang=60,  x=0, y=0):

    t.begin_fill()
    t.teleport(x,y)
    t.fd(r)
    t.lt(90)
    t.circle(r, ang)
    t.lt(90)
    t.fd(r)
    
    t.end_fill()
    t.lt(360 - (180+ang))

    return 

def square(t: turtle.Turtle, side, ang=0, x=0,y=0):

    t.teleport(x, y)
    t.setheading(ang)
    for i in range(4):
        t.fd(side)
        t.rt(90)

    

t = turtle.Turtle()
t.pen(fillcolor="yellow", pencolor="black", pensize=2)

t.teleport(-110,0)
t.rt(90)

t.begin_fill()
for i in range(4):    
    t.fd(110)
    t.lt(90)
    t.fd(110)
t.end_fill()
t.setheading(0)
t.teleport(0,0)

t.pen(fillcolor="black", pencolor="yellow", pensize=5)

arc(t)
t.setheading(120)
arc(t)
t.setheading(240)
arc(t)


t.setheading(270)
t.teleport(-20,0)
t.begin_fill()
t.circle(20,)
t.end_fill()

# t.hideturtle()

turtle.exitonclick()
import turtle


def circle(t: turtle.Turtle, r=100, color="black",  x=0, y=0, thick=5):

    t.teleport(x,y)
    t.color(color)
    t.pensize(thick)
    t.circle(radius=r)

    return 

def square(t: turtle.Turtle, side, ang=0, x=0,y=0):

    t.teleport(x, y)
    t.setheading(ang)
    for i in range(4):
        t.fd(side)
        t.rt(90)

t = turtle.Turtle()

circle(t, r=50, color="blue", x=-110, y=50)
circle(t, r=50, color="black", x=0, y=50)
circle(t, r=50, color="red", x=110, y=50)

circle(t, r=50, color="yellow", x=-60)
circle(t, r=50, color="green", x=60)

t.hideturtle()

turtle.exitonclick()
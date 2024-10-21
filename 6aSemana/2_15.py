import turtle



def square(t: turtle.Turtle, side, ang=0, x=0,y=0):
    """
     @t : turtle.Turtle
    """

    t.teleport(x, y)
    t.setheading(ang)
    for i in range(4):
        t.fd(side)
        t.rt(90)



t = turtle.Turtle()

for i in range(5, 275, 10):
    square(t,i, i)

turtle.exitonclick()
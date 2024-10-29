import turtle

def arc(t, l):


    t.begin_fill()
    t.fd(l)
    t.lt(90)
    t.circle(l, 60)
    t.lt(90)
    t.fd(l)
    t.end_fill()


t = turtle.Turtle()
l = 100


t.color("white", "black")
arc(t, l)

t.teleport(100, 100)
arc(t, l)

t.teleport(-100, -100)
arc(t, l)


turtle.exitonclick()
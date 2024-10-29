import turtle

t = turtle.Turtle()


def arco(lado):
    t.begin_fill()
    t.fd(lado)
    t.left(90)
    t.circle(lado, 60)
    t.left(90)
    t.fd(lado)
    t.end_fill()

    return


def my_circle(lado):
    t.begin_fill()
    t.circle(lado)
    t.end_fill()

    return



lado = 100
arco(lado)
arco(lado)
arco(lado)


t.pen(fillcolor="black", pencolor="yellow", pensize=5)
my_circle(20)


turtle.exitonclick()
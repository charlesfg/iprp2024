import turtle


def tri(n):
    for i in range(3):
        turtle.fd(n)
        turtle.rt(120)

n = 25
a = 360/n
for i in range(n):
    tri(100)
    turtle.rt(a)

turtle.exitonclick()


import turtle

t = turtle.Turtle()


l = 100

def triangle(t, l=50):
    for i in range(3):
        t.fd(l)
        t.rt(120)

for i in range(6):
    triangle(t,l)
    t.rt(60)

t.hideturtle()

turtle.exitonclick()
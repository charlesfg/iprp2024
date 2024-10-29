import turtle




def square(t, cell, x, y):
    t.teleport(x, y)
    for i in range(4):
        t.fd(cell)
        t.rt(90)





def grelha(t, dim, cell):
    t.teleport(-(dim*cell//2), -(dim*cell//2))
    inipos = t.pos()
    for i in range(dim):
        for j in range(dim):
            square(t, cell, inipos[0]+(i*cell), inipos[1]+(j*cell))
        


t = turtle.Turtle()
#turtle.delay(1)
turtle.tracer(1,1)
t.color("light gray")

grelha(t, 5, 20)

turtle.exitonclick()
import turtle

t = turtle.Turtle()
turtle.colormode(255)
print(turtle.screensize())
# turtle.screensize(canvwidth=800, canvheight=800) 
# turtle.setworldcoordinates(-200, -200, 200, 200)
print(t.pos())

def concentricos(t, x, y, n, l, s):
    """
    Desenha n quadrados concentricos na posição x, y 
    com o maior com lado l e step decremental de s
    """
    t.teleport(x, y)
    t.pu()
    t.fd(l//2)
    t.pd()
    color_base = 255
    color_step = 256//n

    cl  = l
    for i in range(n):
        c = color_base - color_step * (i+1)

        t.fillcolor((c,c,c))
        t.begin_fill()
        for j in range(4):
            t.fd(cl)
            t.rt(90)
        t.pu()
        t.fd(s//2)
        t.rt(90)
        t.fd(s//2)
        t.rt(270)
        t.pd()
        cl = cl - s
    
print(t.pos())

concentricos(t, -500, 250, 10, 500, 48)
print(t.pos())
t.hideturtle()

turtle.exitonclick()
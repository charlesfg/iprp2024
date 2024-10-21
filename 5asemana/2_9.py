import turtle

t = turtle.Turtle()




print(turtle.screensize())

turtle.screensize(canvwidth=1400, canvheight=1400, 
                  bg="blue") 
turtle.setworldcoordinates(-700, -700, 700, 700)

t.shape('turtle')
t.color("red")

def spiral(t, ticks, inc):
    t.pu()
    for i in range(ticks):
        
        t.fd(inc * i)
        t.rt(30)
        t.stamp()


spiral(t, 50, 10)


turtle.exitonclick()
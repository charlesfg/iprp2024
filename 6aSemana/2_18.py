import turtle

def half_yy(t:turtle.Turtle,radius, 
            fillcollor="white",pencolor="black", 
            x=None, y=None
    ):
    
    if x and y:
        t.teleport(x, y)
    
    
    t.color(pencolor, fillcollor)
    t.begin_fill()

    t.rt(90)
    t.circle(radius, 180)
    t.rt(-180)
    t.circle(radius, -180)

    
    t.penup()
    t.left(90)
    t.fd(radius)
    t.dot((radius/10)*3, pencolor)
    t.rt(180)
    t.fd(radius)
    t.left(90)
    t.pendown()

    t.circle(2*radius,-180)

    t.end_fill()


def yy(t : turtle.Turtle, radius, x, y):

    t.teleport(x,y)
    half_yy(t,radius)
    t.penup()
    t.lt(90)
    t.fd( 4 *radius)
    t.lt(180)
    t.pendown()
    half_yy(t,radius,fillcollor="black", pencolor="white")



t = turtle.Turtle()

def move(t, d):
    t.penup()
    t.rt(30)
    t.fd(d * 1.35)
    t.pendown()


turtle.screensize(canvwidth=1400, canvheight=1400) 
turtle.resizemode("auto")


for i in range(10, 200, 3):
    move(t, i)
    yy(t,i, t.xcor(), t.ycor())
    





turtle.exitonclick()
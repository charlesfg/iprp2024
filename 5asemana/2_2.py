import turtle

# https://docs.python.org/3/library/turtle.html


def figura(l, n, a, inc):
    """
    Desenha uma figura de com um traço l e virando um angulo de a graus n vezes
    """
   
    for i in range(n):
        turtle.fd(l)
        l = l+inc
        turtle.right(a)
    
    
turtle.penup()
turtle.goto(-50,0)
turtle.pendown()
n = 50
ang = int(180-(180/9))
figura(10, n, ang, 10)
turtle.hideturtle()

turtle.exitonclick()
import turtle


def figura(l, n, a):
    """
    Desenha uma figura de com um traço l e virando um angulo de a graus n vezes
    """
   
    for i in range(n):
        turtle.fd(l)
        turtle.right(a)
    
    
turtle.setworldcoordinates(-500,-500,500,500)
turtle.goto(-250,0)
n = 13
figura(500, n, int(180-(180/n)))
#figura(350, 12, 76)

turtle.exitonclick()
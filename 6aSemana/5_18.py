import turtle



def grelha(t: turtle.Turtle, l,w, cd):

    t.setheading(0)

    pos = t.pos()

    if l % cd != 0 or w % cd != 0:
        raise ValueError("Tamanho da grelha tem que ser proporcional")
    
    for i in range(2):
        t.fd(w)
        t.lt(90)
        t.fd(l)
        t.lt(90)

    cur_direction = -1
    for i in range( w // cd):
        t.fd(cd)
        cur_direction *= -1
        t.goto(t.xcor(), t.ycor() + l * cur_direction)

    
    
      
    t.lt(90)

    t.penup()
    t.setpos(pos)
    t.pendown()
    cur_direction = -1 

    for i in range(1, l // cd):
        t.fd(cd)
        cur_direction *= -1 
        t.goto(t.xcor() + w * cur_direction, t.ycor())


    



t = turtle.Turtle()
t.teleport(-20, -20)
t.color("light gray")
grelha(t, 100,100,20)
# t.clear()
# grelha(t, 120,100,20)
# t.clear()

# grelha(t, 180,100,20)



turtle.exitonclick()
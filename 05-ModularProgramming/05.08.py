def drawSquare(x,y,n):
    import turtle
    for _ in range(1):
        turtle.penup()
        turtle.setposition(x,y)
    for _ in range(1,25):
        if _%10==0:
            turtle.pendown()
            turtle.left(90)
            turtle.forward(n)
            turtle.left(90)
        elif _%5==0:
            turtle.pendown()
            turtle.right(90)
            turtle.forward(n)
            turtle.right(90)
        else:
            turtle.pendown()
            turtle.forward(n)
    turtle.left(90)     
    for _ in range(1,25):
        if _%10==0:
            turtle.pendown()
            turtle.right(90)
            turtle.forward(n)
            turtle.right(90)
        elif _%5==0:
            turtle.pendown()
            turtle.left(90)
            turtle.forward(n)
            turtle.left(90)
        else:
            turtle.pendown()
            turtle.forward(n)
drawSquare(-475,400,100)
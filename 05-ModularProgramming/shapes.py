import turtle
def drawSquare(x,y,n):
    for _ in range(1):
        turtle.penup()
        turtle.setposition(x,y)
    turtle.fillcolor('black')
    turtle.begin_fill()
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
    turtle.end_fill()

def drawCircle(r,x,y):
    turtle.penup()
    turtle.setposition(x,y)
    turtle.pendown()
    turtle.circle(r)

def drawTriangle(m,x,y):
    turtle.penup()
    turtle.setposition(x,y)
    turtle.pendown()
    for _ in range(3):
        turtle.forward(m)
        turtle.left(120)

def drawStar():
    for _ in range(5):
        turtle.forward(100)
        turtle.right(144)

def drawBlackSquare(m):
    turtle.fillcolor("black")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(m)
        turtle.right(90)
    turtle.end_fill()
    
def drawChessboard(m):
    turtle.penup()
    turtle.setposition(-395,404)
    turtle.pendown()
    turtle.fillcolor('black')
    turtle.begin_fill()
    for _ in range(1,81):
        if _%18==0:
            turtle.left(90)
            turtle.forward(n)
            turtle.left(90)
        elif _%9==0:
            turtle.right(90)
            turtle.forward(n)
            turtle.right(90)
        else:
            turtle.forward(n)
    turtle.left(90)     
    for _ in range(1,81):
        if _%18==0:
            turtle.right(90)
            turtle.forward(n)
            turtle.right(90)
        elif _%9==0:
            turtle.left(90)
            turtle.forward(n)
            turtle.left(90)
        else:
            turtle.forward(n)
    turtle.end_fill()
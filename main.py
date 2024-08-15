import turtle

def draw_rectangle(color, width, height):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_chakra():
    turtle.penup()
    turtle.goto(0, -30)
    turtle.pendown()
    turtle.color("navy")
    turtle.width(3)
    turtle.circle(30)
    turtle.width(2)
    for _ in range(24):
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.forward(30)
        turtle.right(15)

def draw_pole():
    turtle.penup()
    turtle.goto(-160, 100)
    turtle.pendown()
    turtle.color("saddlebrown")
    turtle.begin_fill()

    turtle.right(90)       
    turtle.forward(400)    
    turtle.left(90)       
    turtle.forward(10)   
    turtle.left(90)       
    turtle.forward(400)    
    turtle.left(90)        
    turtle.forward(10)     

    turtle.end_fill()

def draw_indian_flag():
    turtle.speed(3)
    turtle.width(2)

    turtle.penup()
    turtle.goto(-150, 100)
    turtle.pendown()
    draw_rectangle("orange", 300, 67)

    turtle.penup()
    turtle.goto(-150, 33)
    turtle.pendown()
    draw_rectangle("white", 300, 67)

    turtle.penup()
    turtle.goto(-150, -34)
    turtle.pendown()
    draw_rectangle("green", 300, 67)

    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    draw_chakra()

    draw_pole()

    turtle.hideturtle()
    turtle.done()

draw_indian_flag()

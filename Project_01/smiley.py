import turtle
def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

    turtle.setup(width= 800, height=600)
    turtle.bgcolor("white")
    
    turtle.penup()
    turtle.speed(2)

    draw_circle("yellow", 150, 0, -150)

    draw_circle("black", 20, -50, 30)
    draw_circle("black", 20, 50, 30)

    draw_circle("white", 5, -50, 30)
    draw_circle("white", 5, 50, 30)

    turtle.penup()
    turtle.goto(-65, -15)
    turtle.pendown()
    turtle.setheading(-60)
    turtle.circle(75, 130)

    turtle.hideturtle()
    turtle.exitonclick()
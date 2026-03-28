import turtle

screen = turtle.Screen()
screen.bgcolor("white")
turtle.tracer(0,0)

def draw_square(x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()

def draw_circle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_triangle(x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()

def draw_ornament():
    colors = ["red", "green", "orange"]
    for row in range(-150, 151, 100):
        for col in range(-200, 201, 100):
            draw_square(col, row, 40, colors[0])
            draw_circle(col + 20, row - 20, 20, colors[1])
            draw_triangle(col, row, 40, colors[2])

draw_ornament()
turtle.done()
import turtle
turtle.tracer(0,0)

def draw_triangle(x1, y1, x2, y2, x3, y3, color):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.goto(x1, y1)
    turtle.end_fill()

def draw_square(x, y, size, color1, color2):

    draw_triangle(x, y, x + size, y, x + size, y - size, color1)
    draw_triangle(x, y, x, y - size, x + size, y - size, color2)

def draw_pattern():
    size = 50
    for row in range(8):
        for col in range(8):

            if row == col or row + col == 7:
                c1, c2 = "darkblue", "darkblue"

            elif (row + col) % 2 == 0:
                c1, c2 = "blue", "lightblue"
            else:
                c1, c2 = "lightblue", "blue"

            draw_square(-200 + col * size, 200 - row * size, size, c1, c2)

turtle.speed(0)
draw_pattern()
turtle.done()
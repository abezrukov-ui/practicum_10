import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
turtle.speed(0)

def draw_building(x, y, width, height, color="dimgray"):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_windows(x, y, width, height, rows, cols):
    turtle.color("yellow")
    for i in range(rows):
        for j in range(cols):
            if random.choice([True, False]):
                wx = x + j * (width // cols) + 5
                wy = y + i * (height // rows) + 5
                turtle.penup()
                turtle.goto(wx, wy)
                turtle.pendown()
                turtle.begin_fill()
                for _ in range(4):
                    turtle.forward(10)
                    turtle.left(90)
                turtle.end_fill()

def draw_stars(count):
    turtle.color("white")
    for _ in range(count):
        sx = random.randint(-300, 300)
        sy = random.randint(50, 300)
        turtle.penup()
        turtle.goto(sx, sy)
        turtle.pendown()
        turtle.dot(random.randint(2, 4))

def draw_cityscape():
    draw_stars(100)
    buildings = [(-300, -200, 80, 150),
                 (-200, -200, 100, 220),
                 (-50, -200, 120, 180),
                 (100, -200, 90, 250),
                 (220, -200, 80, 160)]
    for b in buildings:
        draw_building(*b)
        draw_windows(b[0], b[1], b[2], b[3], rows=8, cols=5)

draw_cityscape()
turtle.done()